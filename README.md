\# AI Lead Outreach Automation



!\[n8n](https://img.shields.io/badge/n8n-Automation-FF6D5A?logo=n8n\&logoColor=white)

!\[Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?logo=google\&logoColor=white)

!\[Google Sheets](https://img.shields.io/badge/Google-Sheets-34A853?logo=googlesheets\&logoColor=white)

!\[Gmail](https://img.shields.io/badge/Gmail-API-EA4335?logo=gmail\&logoColor=white)

!\[License](https://img.shields.io/badge/License-MIT-green)



An AI-powered lead outreach automation workflow built with \*\*n8n\*\*, \*\*Google Gemini\*\*, \*\*Google Sheets\*\*, and \*\*Gmail\*\*.



This project demonstrates how AI can automate the lead outreach process by generating personalized emails, managing outreach status, and handling execution tracking with minimal human intervention.



\---



\# Overview



Manual lead outreach is repetitive, time-consuming, and difficult to scale.



This workflow automates the entire outreach pipeline by:



\- Reading leads from Google Sheets

\- Filtering only pending leads

\- Generating personalized emails using Google Gemini

\- Creating Gmail drafts or sending emails automatically

\- Updating each processed lead with execution details

\- Logging failures for troubleshooting



\---



\# Features



\- 🤖 AI-powered personalized email generation

\- 📊 Google Sheets as a lightweight CRM

\- 📧 Supports both Gmail Draft Mode and Send Mode

\- ✅ Automatic lead status management

\- 📝 Execution ID tracking

\- ⏱ Processing timestamps

\- ⚠ Error logging

\- 🔄 Retry mechanism for temporary failures

\- 🧩 Modular workflow architecture

\- 📈 Easy to extend with additional integrations



\---



\# Workflow Architecture



<p align="center">

&#x20;   <img src="images/workflow.png" width="100%">

</p>



The workflow begins by reading pending leads from Google Sheets. Each lead is processed individually, where Google Gemini generates a personalized outreach email. Depending on the selected mode, the workflow either creates a Gmail draft or sends the email directly. Finally, the lead information is updated with execution status, timestamps, execution IDs, and error logs.



\---



\# Technology Stack



| Category | Technology |

|----------|------------|

| Workflow Automation | n8n |

| Artificial Intelligence | Google Gemini |

| Lead Database | Google Sheets |

| Email Service | Gmail API |

| Version Control | Git |

| Repository | GitHub |



\---



\# Project Structure



```text

AI-Lead-Outreach-Automation

│

├── images

│   ├── workflow.png

│   ├── google\_sheet\_before.png

│   ├── google\_sheet\_after.png

│   ├── gmail\_draft\_total.png

│   └── gmail\_draft\_content.png

│

├── workflow

│   └── AI Lead Outreach Automation.json

│

├── README.md

├── LICENSE

└── .gitignore

```



\---



\# Screenshots



\## Workflow



<p align="center">

&#x20;   <img src="images/workflow.png" width="100%">

</p>



\---



\## Google Sheet (Before Processing)



<p align="center">

&#x20;   <img src="images/google\_sheet\_before.png" width="100%">

</p>



\---



\## Google Sheet (After Processing)



<p align="center">

&#x20;   <img src="images/google\_sheet\_after.png" width="100%">

</p>



\---



\## Gmail Draft



<p align="center">

&#x20;   <img src="images/gmail\_draft\_total.png" width="100%">

</p>



\---



\## Generated Email Content



<p align="center">

&#x20;   <img src="images/gmail\_draft\_content.png" width="100%">

</p>



\---



\# How It Works



1\. Read all leads from Google Sheets.

2\. Filter only rows marked as \*\*Pending\*\*.

3\. Generate a personalized email using Google Gemini.

4\. Choose between:

&#x20;  - Draft Mode

&#x20;  - Send Mode

5\. Update the processed row with:

&#x20;  - Status

&#x20;  - Email Subject

&#x20;  - Processed Timestamp

&#x20;  - Execution ID

6\. If an error occurs:

&#x20;  - Log the error message

&#x20;  - Mark the row as failed

&#x20;  - Store execution information



\---



\# Error Handling



The workflow contains a dedicated error handling branch.



Implemented mechanisms include:



\- Automatic retries

\- Error logging

\- Failed lead tracking

\- Execution ID recording

\- Status updates

\- Safe workflow continuation



\---



\# Future Improvements



Potential future enhancements include:



\- HubSpot integration

\- Salesforce integration

\- Airtable support

\- AI-powered lead scoring

\- Automatic follow-up sequences

\- Email template A/B testing

\- Analytics dashboard

\- Multi-language support

\- Multiple AI provider support (OpenAI, Claude, Gemini)



\---



\# Getting Started



\### Requirements



\- n8n

\- Google Sheets API

\- Gmail API

\- Google Gemini API



\### Import Workflow



1\. Download the workflow JSON.

2\. Open n8n.

3\. Import the workflow.

4\. Configure your credentials.

5\. Update the Google Sheet ID.

6\. Execute the workflow.



\---



\# License



This project is licensed under the MIT License.

