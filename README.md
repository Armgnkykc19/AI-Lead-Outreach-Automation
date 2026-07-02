# AI Lead Outreach Automation

![n8n](https://img.shields.io/badge/n8n-Automation-FF6D5A?logo=n8n&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?logo=google&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google-Sheets-34A853?logo=googlesheets&logoColor=white)
![Gmail](https://img.shields.io/badge/Gmail-API-EA4335?logo=gmail&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub last commit](https://img.shields.io/github/last-commit/Armgnkykc19/AI-Lead-Outreach-Automation)

An AI-powered lead outreach automation workflow built with **n8n**, **Google Gemini**, **Google Sheets**, and **Gmail**.

This project automates the complete lead outreach pipeline by reading leads from Google Sheets, generating personalized cold emails with AI, creating Gmail drafts or sending emails automatically, and updating execution status back to the spreadsheet.

---

# 🎬 Live Demo

<p align="center">
  <img src="images/demo.gif" alt="Workflow Demo" width="1000">
</p>

---

# Features

- 🤖 AI-powered email generation using Google Gemini
- 📊 Google Sheets as a lightweight CRM
- 📧 Draft Mode & Send Mode
- ✅ Automatic lead status updates
- 📝 Execution ID tracking
- ⏱ Process timestamps
- ⚠️ Error logging
- 🔄 Automatic retry mechanism
- 🧩 Modular workflow architecture
- 📈 Easy to extend with new integrations

---

# Workflow Architecture

<p align="center">
<img src="images/workflow.png" width="1000">
</p>

The workflow performs the following steps:

1. Read leads from Google Sheets.
2. Filter leads marked as **pending**.
3. Generate a personalized email using Google Gemini.
4. Create a Gmail Draft or send the email directly.
5. Update the lead status and execution metadata.
6. Handle failures automatically.

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Workflow Automation | n8n |
| Artificial Intelligence | Google Gemini |
| Database | Google Sheets |
| Email | Gmail API |
| Version Control | Git |
| Repository | GitHub |

---

# Project Structure

```text
AI-Lead-Outreach-Automation
│
├── images
│   ├── demo.gif
│   ├── workflow.png
│   ├── google_sheet_before.png
│   ├── google_sheet_after.png
│   ├── gmail_draft_total.png
│   └── gmail_draft_content.png
│
├── workflow
│   └── AI Lead Outreach Automation.json
│
├── sample
│   └── sample_leads.csv
│
├── INSTALLATION.md
├── README.md
├── LICENSE
└── .gitignore
```

---

# Screenshots

## Workflow

<p align="center">
<img src="images/workflow.png" width="1000">
</p>

---

## Google Sheet (Before Processing)

<p align="center">
<img src="images/google_sheet_before.png" width="1000">
</p>

---

## Google Sheet (After Processing)

<p align="center">
<img src="images/google_sheet_after.png" width="1000">
</p>

---

## Gmail Draft

<p align="center">
<img src="images/gmail_draft_total.png" width="1000">
</p>

---

## Generated Email Content

<p align="center">
<img src="images/gmail_draft_content.png" width="1000">
</p>

---

# Configuration

Before running the workflow:

- Configure Google Sheets credentials.
- Configure Gmail credentials.
- Configure Google Gemini credentials.
- Update the placeholder Google Sheet ID.
- Configure the sender profile inside the **Configuration** node.

---

# Included Resources

- 📄 Public n8n workflow template
- 📊 Sample lead dataset (`sample/sample_leads.csv`)
- 📖 Installation guide (`INSTALLATION.md`)
- 🖼️ Workflow and execution screenshots

---

# Error Handling

Implemented mechanisms:

- Automatic retries
- Failed lead tracking
- Error logging
- Execution ID recording
- Safe workflow continuation
- Automatic status updates

---

# Future Improvements

- HubSpot Integration
- Salesforce Integration
- Airtable Support
- AI Lead Scoring
- Automated Follow-up Emails
- Email A/B Testing
- Analytics Dashboard
- Multi-language Support
- Multiple AI Providers (OpenAI, Claude, Gemini)

---

# Getting Started

1. Clone this repository.
2. Follow the setup instructions in **INSTALLATION.md**.
3. Import the workflow into n8n.
4. Configure your credentials.
5. Update the Google Sheet ID.
6. Configure the sender profile.
7. Execute the workflow.

---

# License

This project is licensed under the **MIT License**.