# Installation Guide

## Prerequisites

Before running the workflow, make sure you have:

- n8n installed
- A Google account
- Google Sheets API credentials
- Gmail API credentials
- Google Gemini API access

---

## Import the Workflow

1. Download the workflow JSON file.
2. Open your n8n instance.
3. Click **Import from File**.
4. Select **AI Lead Outreach Automation.json**.

---

## Configure Credentials

Create and configure the following credentials inside n8n:

- Google Sheets OAuth2
- Gmail OAuth2
- Google Gemini API

Assign the credentials to the corresponding nodes.

---

## Configure the Workflow

Update the placeholder values:

- Google Sheet ID
- Sender Name
- Sender Title
- Sender Company
- Sender Email
- Signature closing lines and signature block

- Email Language (`email_language`) — `Turkish`, `English`, or blank to let the AI
  follow the language of the topic
- Signature (`signature_closing_en`, `signature_closing_tr`, `signature_block`) —
  the closing line follows the email language automatically; the block below it
  (name, title, company) is used as-is in every language
- Campaign Topic (`campaign_topic`) — default topic used when a row leaves `topic` blank
- Campaign Subject Prefix (`campaign_subject_prefix`) — optional prefix for every subject

These values can be modified inside the **Configuration** node.

---

## Prepare Your Google Sheet

Use the provided **sample/sample_leads.csv** file as a template.

Required columns (you fill these in):

- company
- website
- industry
- city
- score
- recipient_email
- status

Optional campaign columns (you fill these in, leave blank to let the AI decide):

- **topic** — what the email should be about, e.g. `automating warranty claim intake`.
  If blank, the AI picks an automation opportunity based on the company's industry.
- **subject_override** — the exact subject line to use.
  If blank, the AI writes the subject line itself.

Columns written by the workflow (do not edit by hand):

- email_subject — the subject line that was actually used
- subject_source — `manual` if subject_override was used, `ai` if the AI wrote it
- topic_used — the topic that was applied: the row's own topic, the campaign
  default from the Configuration node, or `ai-choice` when none was given
- processed_at, error_message, execution_id

Column order does not matter; the workflow matches columns by their header name.

Set the status column to **pending** for leads that should be processed.

---

## Run

Click **Execute Workflow**.

The workflow will:

1. Read pending leads.
2. Generate personalized emails.
3. Create Gmail drafts or send emails.
4. Update execution status.
5. Log any failures automatically.
