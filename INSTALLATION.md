\# Installation Guide



\## Prerequisites



Before running the workflow, make sure you have:



\- n8n installed

\- A Google account

\- Google Sheets API credentials

\- Gmail API credentials

\- Google Gemini API access



\---



\## Import the Workflow



1\. Download the workflow JSON file.

2\. Open your n8n instance.

3\. Click \*\*Import from File\*\*.

4\. Select \*\*AI Lead Outreach Automation.json\*\*.



\---



\## Configure Credentials



Create and configure the following credentials inside n8n:



\- Google Sheets OAuth2

\- Gmail OAuth2

\- Google Gemini API



Assign the credentials to the corresponding nodes.



\---



\## Configure the Workflow



Update the placeholder values:



\- Google Sheet ID

\- Sender Name

\- Sender Title

\- Sender Company

\- Sender Email

\- Email Signature



These values can be modified inside the \*\*Configuration\*\* node.



\---



\## Prepare Your Google Sheet



Use the provided \*\*sample/sample\_leads.csv\*\* file as a template.



Required columns:



\- company

\- website

\- industry

\- city

\- score

\- recipient\_email

\- status



Set the status column to \*\*pending\*\* for leads that should be processed.



\---



\## Run



Click \*\*Execute Workflow\*\*.



The workflow will:



1\. Read pending leads.

2\. Generate personalized emails.

3\. Create Gmail drafts or send emails.

4\. Update execution status.

5\. Log any failures automatically.

