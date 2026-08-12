---
title: "FCAJ Community Day - June 2026"
date: 2026-06-01
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# Event Report: "FCAJ Community Day - June 2026"

### Objectives of the Event

- Share practical experiences, insights, and real-world perspectives from the enterprise environment on the application of AI and Cloud Computing.
- Introduce advanced and trending technology solutions: Voice AI, DevOps AI Agent (Automating infrastructure operations), and Amazon Q/Quick (Smart assistant for businesses).
- Guide the career path for IT students, especially seniors preparing to enter the labor market.
- Create a space for direct networking and connection between the tech community, students, and experts from major organizations (AWS, R AI, Cloud Thinker, Noventic, Renova Cloud).

### List of Speakers

- **Steve Tran** - Founder & CEO at Cloud Thinker.
- **Hieu Nghi** - Tech Expert from Renova Cloud / AWS Study Builder.
- **Kiet** - Representative from Student Video Group.
- **Trung Nguyen** - Founder & CEO at R AI (Former tech startup founder in the US, invested by YC and acquired by a Google subsidiary).
- **Nguyen Nguyen** & **Bao** - Cloud Engineers from Cloud Kinetics.
- **Truong (Wynn)** & **Minh Anh** - AI Solution Architects / Solutions Shares from Noventic.
- **Toan Nguyen** - AWS Security Builder.

### Key Highlights

#### Session 1: Cloud & AI Agents Modernization - Enterprise Perspectives and Career Orientation

- **Technical Debt and Complexity:** As enterprise systems (e.g., banking, finance) grow and migrate to Cloud, complexity increases, leading to "technical debt." Businesses have to spend significant costs on personnel (DevOps, SRE, NOC) and monitoring tools (Observability Tools).
- **Hiring Trends in the AI Era:** The market is saturated with entry-level developers. Companies tend to pause mass hiring or prioritize hiring Senior engineers capable of coordinating and utilizing AI tools to optimize productivity.
- **Multi-Agent vs. Super Agent Architectures:**
  - *Multi-Agent Architecture:* Helps optimize costs (using small models for simple tasks, large models for reasoning) and avoids Context dilution. Supports Role-Based Access Control (RBAC) across business boundaries. However, the downside is that it is difficult to develop and maintain.
  - *Single Super Agent:* If designed well enough, it can handle over 95% of complex tasks and optimizes Time-to-Resolution.

#### Session 2: Voice AI Agent Mechanism in Vietnamese

- **Challenges with Vietnamese:** Vietnamese is a low-resource language, and the world's large direct Speech-to-Speech translation models are primarily optimized for English.
- **Optimized Voice Bot Architecture for Vietnamese Enterprises:** Uses a 3-component bridge model **(Speech-to-Text → LLM Text Processing → Text-to-Speech)**. This architecture helps businesses strictly control Output content (Guardrails), preventing AI from making misleading statements in sensitive industries like Banking (e.g., VPBank, VIB).
- **Real-time Context Processing Techniques:**
  - Applied continuous data Streaming mechanisms on all 3 ends to minimize Latency.
  - Integrated supplementary Models for gender recognition (to use appropriate pronouns), natural Barge-in handling when customers are speaking, or inserting phone numbers.
  - Managed intelligent Human-in-the-loop transition scenarios when encountering intense customer complaints.

#### Session 3: Applying DevOps AI Agents in Operations and Infrastructure Incident Response

- **Pain Points of Operations Engineers:** Monitoring data is fragmented (Fragmented Telemetry) across multiple places (CloudWatch, CloudTrail...), and lack of domain knowledge between teams prolongs the Mean Time To Detect (MTTD) and Mean Time To Resolve (MTTR).
- **Automated Incident Response Process of DevOps Agent (4 steps):**
  1. *Triage:* Automatically triggers upon system Alert, synthesizing Logs/Traces.
  2. *Investigation:* Based on the system architecture map (Topology) to formulate hypotheses and prove them using Log evidence to find the Root Cause Analysis (RCA).
  3. *Mitigation:* Proposes a step-by-step resolution plan for engineers to approve and execute (ensuring Safety).
  4. *Improvement:* Automatically suggests configuration optimizations based on history to prevent recurring errors.
- **Real-world Case Studies:**
  - WGU Online University reduced incident response time from 2 hours to 28 minutes (77% faster).
  - KDDI Telecom (Japan) shortened investigation time from weeks to days.

#### Session 4: HR Process Automation & Internal Security Connection with Amazon Q/Quick

- **Applications in HR:** Setting up the "HR Talent Review Assistant" Skill helps automate writing standard JDs, bulk scanning CVs (excellent OCR for scanned/pdf files), scoring matching levels against hard criteria rather than subjective feelings, generating visual HTML reports, and auto-syncing to Google Drive/OneDrive.
- **Enterprise Security Problem:** When integrating AI Agents with third-party systems (Zalo, WhatsApp, Jira...) via MCP (Model Context Protocol) Server, opening a Public Endpoint creates severe security vulnerabilities (like DOS attacks or Man-in-the-middle).
- **Private Connection Solution:** Bringing AI Agents into the internal AWS network by setting up a **VPC Connection**, combined with Route 53 Resolver, Application Load Balancer (ALB) with TLS encryption, and AWS Secrets Manager. The entire data flow of querying Metrics and System Logs is completely encapsulated within the AWS Private network, bypassing the public Internet entirely.

### What I Learned

#### Regarding Design Thinking & Strategy

- **Business-First Approach:** System design or AI application must originate from practical problems and business workflows (e.g., bank debt collection, HR resume filtering); technology is merely a supporting tool.
- **Forward-Thinking Mindset:** Understanding job market shifts in the AI era. Engineers must not only code but also utilize Agents (Vibe Coding/Prompt Engineering) to drastically increase productivity.
- **Governance & Security Strategy:** Deep awareness of the importance of protecting internal data when applying AI, adhering to Zero Trust principles, and establishing approval layers before AI intervenes in the Production environment.

#### Regarding Technical Architecture

- Mastered the Voice AI coordination architecture: STT → LLM → TTS with latency-reducing Streaming techniques.
- Understood how DevOps Agents operate through Agent Space and system Topology mapping mechanisms.
- Approached the MCP (Model Context Protocol) protocol used to expand AI's flexible connectivity with any third-party tool.
- Grasped the infrastructure deployment model for securing Private Cloud connections using AWS VPC Endpoint and Private DNS Resolver.

### Applications to Work / Internship Project

- **Applying AI to the Software Development Life Cycle (SDLC):** Experimenting with Amazon Q Developer / GitHub Copilot integration into the IDE to assist with code reviews and automated test coverage writing to optimize Quality Control.
- **Designing Event-Driven:** Replacing Synchronous direct calls with Asynchronous message queues to achieve loose coupling, increasing system scalability and fault tolerance.
- **Optimizing Project Workflows:** Applying techniques to configure specialized "Skills" on Chat Agents (like setting up standard formats for essays and reports) to automate internal document processing.
- **Preparing Career Portfolio:** Refining and writing a professional developer CV, focusing on highlighting technical Keywords compatible with target Job Descriptions (JD) to pass AI CV Screening filters of major enterprises today.

### Personal Experience at the Event

Attending the **FCAJ Community Day** was an extremely practical and valuable technical experience. The most impressive aspect was that the program wasn't purely theoretical but illustrated by a series of highly visual **Live Demos**: from a Voice Bot verbally interacting about Apple products, to a simulated DDoS hacker attack on an E-commerce app's ECS Task where a DevOps Agent automatically jumped in to trace the Logs, to hands-on manipulation on the Amazon Quick Desktop interface. The networking atmosphere was vibrant with tough Q&A sessions about Cost Optimization, helping me absorb profound, hard-earned experiences from seasoned experts.

#### Some photos from the event
![Event Image](/aws-image/event1/1786290035581_117422063285167014_2562150942337330825_15bb7201c893376a16de87a95a3357e2.jpg)
![Event Image](/aws-image/event1/1786290035606_117422063285167014_2562150942337330825_7f8192c4c50ecd6f280995f5608d374d.jpg)
![Event Image](/aws-image/event1/1786290035633_117422063285167014_2562150942337330825_ab8387e8923e50641d53c500dabacabf.jpg)
![Event Image](/aws-image/event1/1786290035658_117422063285167014_2562150942337330825_c2542ff656894cf661a9acdf320bb2f1.jpg)
![Event Image](/aws-image/event1/1786290035682_117422063285167014_2562150942337330825_6b6076c1733655bdee5208daf13cd454.jpg)
