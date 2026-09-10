#!/usr/bin/env python3
"""Sync the workflow between this repository and a running n8n instance.

The two copies deliberately hold different things. The repository copy is
sanitised so it can be published: no credential references and a placeholder
Google Sheet ID. The copy inside n8n holds the opposite -- real credential
references and the real Sheet ID. Copying either one straight over the other
destroys information, which is why this script grafts one onto the other
instead of overwriting.

    push  repository structure -> n8n, keeping n8n's credentials and Sheet ID
    pull  n8n structure        -> repository, stripping both back out

Examples:
    python scripts/sync_workflow.py push --workflow-id km4LUKHmCL4cdSd8
    python scripts/sync_workflow.py pull --workflow-id km4LUKHmCL4cdSd8 --dry-run
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_FILE = REPO_ROOT / "workflow" / "AI Lead Outreach Automation.json"
PLACEHOLDER = "YOUR_GOOGLE_SHEET_ID"

# Node parameters that hold the real Sheet ID and are carried over on a push.
SECRET_PARAMS = ("documentId", "sheetName")

EXPRESSION_RE = re.compile(r'"(={{.*?}})"')

Workflow = dict[str, Any]


def run(command: list[str]) -> str:
    """Run a command, raising with the captured stderr when it fails."""
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"{' '.join(command)} failed:\n{result.stderr.strip()}")
    return result.stdout


def export_from_n8n(container: str, workflow_id: str, work_dir: Path) -> Workflow:
    """Export one workflow out of the running container."""
    remote = f"/tmp/n8n-sync-{workflow_id}.json"
    local = work_dir / "live.json"
    run(["docker", "exec", container, "n8n", "export:workflow",
         f"--id={workflow_id}", f"--output={remote}"])
    run(["docker", "cp", f"{container}:{remote}", str(local)])
    exported = json.loads(local.read_text(encoding="utf-8"))
    # export:workflow emits a list even when a single --id is given.
    return exported[0] if isinstance(exported, list) else exported


def import_into_n8n(container: str, workflow: Workflow, work_dir: Path) -> None:
    """Import a workflow. The id travels with it, so this updates in place."""
    local = work_dir / "import.json"
    local.write_text(json.dumps(workflow, indent=2, ensure_ascii=False), encoding="utf-8")
    remote = "/tmp/n8n-sync-import.json"
    run(["docker", "cp", str(local), f"{container}:{remote}"])
    run(["docker", "exec", container, "n8n", "import:workflow", f"--input={remote}"])


def graft_secrets(repo: Workflow, live: Workflow) -> Workflow:
    """Put the repository's structure onto n8n's credentials and Sheet ID.

    Nodes are matched by name rather than id: a node added to the repository
    copy by hand will not carry the id n8n generated for it.
    """
    live_nodes = {node["name"]: node for node in live["nodes"]}
    merged = json.loads(json.dumps(live))
    merged["nodes"] = json.loads(json.dumps(repo["nodes"]))
    merged["connections"] = json.loads(json.dumps(repo["connections"]))

    for node in merged["nodes"]:
        source = live_nodes.get(node["name"])
        if source is None:
            continue  # genuinely new node; n8n assigns an id on import
        node["id"] = source["id"]
        if "credentials" in source:
            node["credentials"] = source["credentials"]
        for key in SECRET_PARAMS:
            if key in source.get("parameters", {}):
                node["parameters"][key] = source["parameters"][key]
    return merged


def sanitise(live: Workflow) -> Workflow:
    """Strip credentials and the real Sheet ID so the result is publishable."""
    clean = json.loads(json.dumps(live))
    real_ids: set[str] = set()

    for node in clean["nodes"]:
        node.pop("credentials", None)
        document = node.get("parameters", {}).get("documentId")
        if isinstance(document, dict) and document.get("value"):
            real_ids.add(str(document["value"]))

    # The id is echoed inside cached display URLs too, so replace it everywhere.
    text = json.dumps(clean, ensure_ascii=False)
    for real_id in real_ids:
        if real_id != PLACEHOLDER:
            text = text.replace(real_id, PLACEHOLDER)
    return json.loads(text)


def check_expressions(workflow: Workflow) -> list[str]:
    """Catch the two ways an expression silently breaks when edited by a script.

    A real newline inside a regex literal is a syntax error at run time, and a
    lost `$` turns `$json.output` into a reference to nothing. Both have
    happened while building this workflow, so they are checked on every push.
    """
    problems: list[str] = []
    for node in workflow["nodes"]:
        rendered = json.dumps(node.get("parameters", {}), ensure_ascii=False)
        for quoted in EXPRESSION_RE.findall(rendered):
            expression = json.loads(f'"{quoted}"')
            if "\r" in expression or "\n" in expression:
                problems.append(f"{node['name']}: literal newline inside an expression")
            if ".output" in expression and "$json.output" not in expression:
                problems.append(f"{node['name']}: expression lost its `$json`")
    return problems


def load_repo_workflow() -> Workflow:
    return json.loads(WORKFLOW_FILE.read_text(encoding="utf-8"))


def save_repo_workflow(workflow: Workflow) -> None:
    WORKFLOW_FILE.write_text(
        json.dumps(workflow, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def do_push(container: str, workflow_id: str, work_dir: Path, dry_run: bool) -> int:
    repo = load_repo_workflow()
    problems = check_expressions(repo)
    if problems:
        print("Refusing to push, the repository copy looks broken:", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1

    live = export_from_n8n(container, workflow_id, work_dir)
    merged = graft_secrets(repo, live)
    kept = sum(1 for node in merged["nodes"] if node.get("credentials"))
    print(f"push: {len(merged['nodes'])} nodes, credentials kept on {kept}")

    if PLACEHOLDER in json.dumps(merged):
        print("Refusing to push: the placeholder Sheet ID survived the merge, "
              "so n8n would lose its real one.", file=sys.stderr)
        return 1
    if dry_run:
        print("dry run, nothing imported")
        return 0

    import_into_n8n(container, merged, work_dir)
    after = export_from_n8n(container, workflow_id, work_dir)
    print(f"verified: n8n now reports {len(after['nodes'])} nodes")
    return 0


def do_pull(container: str, workflow_id: str, work_dir: Path, dry_run: bool) -> int:
    live = export_from_n8n(container, workflow_id, work_dir)
    clean = sanitise(live)

    if any(node.get("credentials") for node in clean["nodes"]):
        print("Refusing to pull: credentials survived sanitising.", file=sys.stderr)
        return 1
    print(f"pull: {len(clean['nodes'])} nodes, credentials stripped, "
          f"Sheet ID replaced with {PLACEHOLDER}")

    if dry_run:
        print("dry run, repository not written")
        return 0

    save_repo_workflow(clean)
    print(f"written to {WORKFLOW_FILE.relative_to(REPO_ROOT)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("direction", choices=("push", "pull"))
    parser.add_argument("--container", default="n8n", help="docker container name")
    parser.add_argument("--workflow-id", required=True, help="n8n workflow id")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if shutil.which("docker") is None:
        print("docker not found on PATH", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory(prefix="n8n-sync-") as tmp:
        action = do_push if args.direction == "push" else do_pull
        try:
            return action(args.container, args.workflow_id, Path(tmp), args.dry_run)
        except RuntimeError as error:
            print(error, file=sys.stderr)
            return 1


if __name__ == "__main__":
    raise SystemExit(main())
