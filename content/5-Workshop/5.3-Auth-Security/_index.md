---
title : "Authentication & Security"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

### Goal

In this section, we will build the first line of defense for user authentication for the entire Smart Campus system. Instead of manually coding password encryption logic and generating complex Tokens, we will fully delegate this to **Amazon Cognito**.

> [!NOTE]
> **AWS WAF** (protecting the API from unauthorized external access) will be configured in **section 5.5.4** — after the API Gateway and Lambda have been created, because WAF requires the API Gateway Invoke URL to operate.

### Detailed Practice Content

Please click on each item below in the left menu bar or click directly on the links below to follow the detailed steps:

{{% children /%}}
