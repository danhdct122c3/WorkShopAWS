---
title: "Week 5: Handle File Uploads (Presigned URL)"
date: 2026-06-22
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

# Week 5: Handle File Uploads (Presigned URL)

**Team Member:** Backend Developer

## 1. Weekly Goals
Handle the file upload problem by issuing Presigned URLs (AWS S3) instead of passing through API Gateway to avoid timeouts and payload limits.

## 2. Detailed Work Log

| Day | Task Description | Start Date | End Date | References |
|---|---|---|---|---|
| Mon | - Analyze the limitations of uploading files via API Gateway (10MB limit). Propose S3 Presigned URL solution. | 20/07/2026 | 20/07/2026 | AWS Docs / Github |
| Tue | - Set up an S3 bucket to store reports. Configure CORS policy so Frontend can perform cross-domain uploads. | 21/07/2026 | 21/07/2026 | StackOverflow |
| Wed | - Write the `/tasks/presigned-url` API calling boto3 `generate_presigned_url` to generate temporary links. | 22/07/2026 | 22/07/2026 | API Docs |
| Thu | - Integrate API to store file metadata (URL, filename) into the Tasks table on DynamoDB. | 23/07/2026 | 23/07/2026 | AWS Blogs |
| Fri | - Set up Content-Type Validation to block malicious file uploads, assist the team in debugging the upload flow. | 24/07/2026 | 24/07/2026 | Weekly Report |


## 3. Achievements
- Completed features and objectives set for the week.
- Successfully integrated with related AWS services (if any).
- Ensured work quality meets project requirements.

## 4. Challenges & Solutions
- **Challenges:** The research and integration process occasionally encountered unexpected errors. Required significant time reading logs and AWS technical documentation.
- **Solutions:** Coordinated with other team members for discussions, thoroughly read the guidelines, and sought additional advice from Mentors.

## 5. Plan for Next Week
- Review this week's completed work.
- Begin research and implementation of tasks for Week 6.

