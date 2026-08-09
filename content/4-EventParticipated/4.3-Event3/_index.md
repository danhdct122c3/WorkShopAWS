---
title: "Agent Forge HCMC Workshop"
date: 2026-08-09
weight: 3
chapter: false
pre: " <b> 4.3. </b> "
---

# SUMMARY REPORT: "AGENT FORGE HCMC WORKSHOP"

### Event Objectives

- Provide foundational and in-depth knowledge about Agentic AI, the shift from static language models (LLMs) to autonomous Agents (AI Agents) capable of reasoning and automating tasks.
- Provide hands-on guidance on the process of building AI Agents on AWS infrastructure using modern tools like Kiro and the AgentCore framework.
- Equip skills to integrate AI systems into real-world enterprise business workflows (e.g., automating the refund process), from setting up memory and connecting knowledge databases to building interfaces and security authorization.

### Speakers

- **Mr. Nghia** – Representative from AWS Study Group (Presented the in-depth Theory section on Agent Core architecture, Runtime, Identity, and Gateway).
- **Mr. Hai Anh** – Representative guiding the Hands-on Labs / Application section.

## PART 1: THEORETICAL FOUNDATION OF AGENTIC AI & SYSTEM ARCHITECTURE (70%)

In the context of rapidly changing technology, Artificial Intelligence Systems are making a strong shift from static language models (LLMs) to autonomous Agents (AI Agents). The workshop provided in-depth theoretical knowledge about the architecture and operation of these Agents.

### 1. Evolution from LLMs to Agentic Workflow

* **Limitations of traditional LLMs:** LLMs (like GPT, Claude) are essentially next-word prediction engines based on trained data. They are passive, lack real-time context, and cannot execute actions (Actionless).
* **The Power of AI Agents:** An Agent is an AI entity capable of perceiving its environment (Perception), logical reasoning (Reasoning/Chain-of-Thought), planning, and using tools to impact the environment. An Agentic Workflow allows AI to automatically break down a complex problem (Task Decomposition), execute step-by-step, self-evaluate results, and correct errors (Self-reflection) until the goal is achieved.

### 2. Three Core Architectural Pillars of an AI Agent

The event delved into the internal architecture of a standard AI Agent used in enterprises:

* **The Brain (LLM):** Acts as the analysis center. It receives the Prompt, determines user intent (Intent Recognition), and decides which tools need to be called.
* **Memory:**
  * *Short-term Memory:* Stores the context of the current session.
  * *Persistent / Long-term Memory:* Stores information across sessions (e.g., purchase history, user preferences). This mechanism is usually implemented via Vector or NoSQL databases (like DynamoDB) so the Agent can retrieve past contexts.

* **Tools & Knowledge:**
  * *Knowledge (RAG - Retrieval-Augmented Generation):* A technique to connect the Agent with the enterprise's private knowledge base, helping AI answer based on internal data instead of pre-trained data, minimizing hallucinations.
  * *Tools/APIs:* Pre-programmed functions for the Agent to call (e.g., API to look up a bill of lading, API to execute a refund command).

### 3. Safe AI Operations & Governance (Governance & Observability)

Deploying AI in an enterprise environment requires strict security and control:

* **AgentCore Policies / Guardrails:** These are hard-coded rules or Prompt Engineering designed to establish "fences" limiting the AI's power. (Example: The Agent is only allowed to propose a refund if the order is not over 30 days old, otherwise it must escalate to a human consultant).
* **Observability:** Tracking how the AI "thinks" (Reasoning Traces) is mandatory. The system must log every reasoning step, which APIs were called, and what payloads were sent, for Audit and Debugging purposes when errors occur.

---

## PART 2: HANDS-ON DEPLOYMENT WITH KIRO & AGENTCORE (30%)

Based on the theoretical foundation above, the practical section (Labs) focused on realizing these concepts using the AWS tool ecosystem, specifically Kiro and the AgentCore framework.

### 1. Agent Setup & Steering

* The practical process began by setting up the AWS Hosted Event DCV environment to ensure infrastructure consistency.
* The focus of Lab 1 was the **Setup Steering** technique in Kiro. This step actualizes the theoretical "Brain," where developers write System Prompts and clearly define the Persona, business boundaries, and standard Output formatting for the Agent.

### 2. Building a Business AI Agent (Returns & Refunds Use-case)

Lab 2 applied the Agentic Workflow model to automate the Returns & Refunds process.

* **Quick Initialization:** The AgentCore Framework allows packaging infrastructure (IaC) and deploying a basic Agent with just 3 command lines, proving the optimization of DevOps processes for AI applications.
* **Realizing Memory & Knowledge:**
  * Integrated Persistent Memory by connecting the Agent with the Amazon DynamoDB database. This allows the Agent to query the real status of orders (Real Data Connection) to decide if they qualify for a refund.

* **Security & Interaction:**
  * Deployed a user interface using Streamlit Chat UI, integrated with Amazon Cognito for access authorization (Authentication), ensuring only valid users can chat with the system.
  * Activated Policies (as learned in the theory section) to prevent the Agent from issuing refunds exceeding limits, while configuring Observability to monitor internal API calls of the agent.

---

## PART 3: LESSONS LEARNED AND PERSONAL APPLICATION ORIENTATION

Through connecting autonomous system theory with AWS practice, the AgentCore architecture opens up many powerful application directions for modern software development:

* **Integrating AI into Microservices Architecture:** When designing Backend systems (e.g., Booking or E-commerce systems), instead of processing all logic with rigid sequential code, I can package the AI Agent into an independent service. This service will communicate with other services (like Product Service, Payment Service) via RESTful APIs or event streaming (Apache Kafka) to handle dynamic, highly analytical operations.
* **Optimizing Database Design for AI:** Practicing with DynamoDB reinforced the mindset of designing non-relational databases (NoSQL) for storing context (Memory) and communication history, which is a mandatory component when designing APIs for AI chatbots.
* **Developing Vibe Coding & DevOps Skills:** Using tools like Kiro or AgentCore Harness helps familiarize oneself with the mindset of using AI to generate code, write tests, and automate the CI/CD deployment pipeline, thereby optimizing the software development lifecycle in preparation for entering real enterprise environments.

#### Some event photos

![Event Image](/aws-image/event3/1786289891441_117422063285167014_2562150942337330825_6e6dda0b3cf7a1ddcaf9ec5689d98f01.jpg)
![Event Image](/aws-image/event3/1786289891501_117422063285167014_2562150942337330825_ed14ca293fbccdc28a4a3f81200354ea.jpg)
![Event Image](/aws-image/event3/1786289891555_117422063285167014_2562150942337330825_cecde5dea800915f41004d0fdb63679f.jpg)
![Event Image](/aws-image/event3/1786289891630_117422063285167014_2562150942337330825_47d4f3fb640da05dc5dfca20cabfba67.jpg)
![Event Image](/aws-image/event3/1786289891685_117422063285167014_2562150942337330825_fcc928389ee2d9d2839ff8ed69791e96.jpg)
![Event Image](/aws-image/event3/1786289891784_117422063285167014_2562150942337330825_97a297edaf0453c7e904709bd0d5b410.jpg)
![Event Image](/aws-image/event3/1786289891844_117422063285167014_2562150942337330825_64344e1f15e8cff2dbc4b526e8c0a7e0.jpg)

