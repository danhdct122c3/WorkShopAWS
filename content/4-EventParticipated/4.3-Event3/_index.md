---
title: "Agent Forge HCMC Workshop"
date: 2026-08-09
weight: 3
chapter: false
pre: " <b> 4.3. </b> "
---

# EVENT SUMMARY REPORT: "AGENT FORGE HCMC WORKSHOP"

### Event Objectives

- Provide foundational and in-depth knowledge about Agentic AI, the shift from static Large Language Models (LLMs) to autonomous AI Agents capable of reasoning and executing tasks autonomously.
- Provide hands-on guidance on the process of building an AI Agent on AWS infrastructure using modern tools like Kiro and the AgentCore framework.
- Equip participants with skills to integrate AI systems into real-world business workflows (e.g., automating refund processes), from setting up memory and connecting to knowledge bases to building user interfaces and securing access control.

### List of Speakers

- **Nghia** – Representative from AWS Study Group (Presented the in-depth Theory section on Agent Core architecture, Runtime, Identity, and Gateway).
- **Hai Anh** – Representative guiding the Hands-on Labs / Application section.

## PART 1: THEORETICAL FOUNDATION OF AGENTIC AI & SYSTEM ARCHITECTURE (70%)

In the context of rapidly changing technology, Artificial Intelligence Systems are shifting strongly from static language models (LLMs) to Autonomous Agents (AI Agents). The workshop provided an in-depth theoretical picture of the architecture and operations of these Agents.

### 1. The Evolution from LLMs to Agentic Workflow

* **Limitations of traditional LLMs:** LLMs (like GPT, Claude) are essentially just next-word prediction machines based on training data. They are passive, lack real-time context, and cannot execute actions (Actionless).
* **The Power of AI Agents:** An Agent is an AI entity capable of perceiving its environment (Perception), logical reasoning (Reasoning/Chain-of-Thought), planning (Planning), and using tools (Tool Use) to interact back with the environment. An Agentic Workflow allows AI to automatically break down a complex problem (Task Decomposition), execute step-by-step, self-evaluate results, and correct errors (Self-reflection) until the goal is achieved.

### 2. The Three Core Architectural Pillars of an AI Agent

The event deeply analyzed the internal architecture of a standard AI Agent used in an enterprise:

* **The Brain (LLM):** Acts as the analysis center. It receives Prompts, identifies user intent (Intent Recognition), and decides which tools need to be called.
* **Memory:**
  * *Short-term Memory:* Stores the context of the current communication session (Session Context).
  * *Persistent / Long-term Memory:* Stores information across sessions (like purchase history, user preferences). This mechanism is often deployed through Vector databases or NoSQL (like DynamoDB) so the Agent can retrieve past context.

* **Tools & Knowledge:**
  * *Knowledge (RAG - Retrieval-Augmented Generation):* Techniques to connect the Agent to the enterprise's private knowledge database, helping the AI answer based on internal data instead of pre-trained data, minimizing "hallucination."
  * *Tools (APIs):* Pre-programmed functions for the Agent to call (e.g., Waybill lookup API, Refund execution API).

### 3. Safe AI Operations and Governance (Governance & Observability)

Bringing AI into an enterprise environment requires strict security and control:

* **AgentCore Policies / Guardrails:** These are hard-coded rules or Prompt Engineering designed to establish "fences" limiting the AI's power. (For example: An Agent is only allowed to propose a refund if the order is not over 30 days old; otherwise, it must transfer to a human consultant).
* **Observability:** Monitoring how the AI "thinks" (Reasoning Traces) is mandatory. The system must log every reasoning step in detail, which API was called, and what the payload sent was, for Audit and Debugging purposes when the system encounters errors.

---

## PART 2: HANDS-ON DEPLOYMENT WITH KIRO & AGENTCORE (30%)

Building on the theoretical foundation, the practical section (Labs) focused on materializing concepts using the AWS tool ecosystem, specifically Kiro and the AgentCore framework.

### 1. Setup and Agent Steering

* The practical process started with setting up the AWS Hosted Event DCV environment to ensure infrastructure consistency.
* The focus of Lab 1 was the **Setup Steering** technique in Kiro. This is the practical realization of "The Brain" theory, where developers write System Prompts and clearly define the Persona, business boundaries, and standard Output formats for the Agent.

### 2. Building a Business AI Agent (Returns & Refunds Use-case)

Lab 2 applied the Agentic Workflow model to automate the Returns & Refunds process.

* **Rapid Initialization:** The AgentCore framework allows packaging infrastructure (IaC) and deploying a basic Agent with just 3 lines of code, demonstrating the optimization of DevOps processes for AI applications.
* **Realizing Memory & Knowledge:**
  * Integrated Persistent Memory by connecting the Agent to the Amazon DynamoDB database. This allows the Agent to query the actual status of orders (Real Data Connection) to decide if they are eligible for a refund.

* **Security & Interaction:**
  * Deployed a user interface using Streamlit Chat UI, combined with Amazon Cognito to grant access permissions (Authentication), ensuring only valid users can chat with the system.
  * Activated Policies (as learned in the theory section) to prevent the Agent from arbitrarily issuing refunds over the limit, while configuring Observability to monitor the agent's internal API call flows.

---

## PART 3: LESSONS LEARNED AND PERSONAL APPLICATION DIRECTIONS

By bridging autonomous system theory with AWS practice, the AgentCore architecture opens up many powerful application directions for modern software development:

* **Integrating AI into  Architecture:** When designing Backend systems (e.g., Booking or E-commerce systems), instead of handling all logic with rigid sequential code, I can package an AI Agent into an independent service. This service will communicate with other services (like Product Service, Payment Service) via RESTful APIs or event streaming (Apache Kafka) to handle dynamic, highly analytical business operations.
* **Optimizing Database Design for AI:** Practicing with DynamoDB helped reinforce non-relational database (NoSQL) design thinking for storing context (Memory) and communication history, which is a mandatory component when designing APIs for AI chatbots.
* **Developing Vibe Coding & DevOps Skills:** Using tools like Kiro or AgentCore Harness helps familiarize with the mindset of using AI to generate code, write tests, and automate CI/CD deployments, thereby optimizing the software development lifecycle in preparation for entering real corporate environments.

#### Some photos from the event

![Event Image](/aws-image/event3/1786289891441_117422063285167014_2562150942337330825_6e6dda0b3cf7a1ddcaf9ec5689d98f01.jpg)
![Event Image](/aws-image/event3/1786289891501_117422063285167014_2562150942337330825_ed14ca293fbccdc28a4a3f81200354ea.jpg)
![Event Image](/aws-image/event3/1786289891555_117422063285167014_2562150942337330825_cecde5dea800915f41004d0fdb63679f.jpg)
![Event Image](/aws-image/event3/1786289891630_117422063285167014_2562150942337330825_47d4f3fb640da05dc5dfca20cabfba67.jpg)
![Event Image](/aws-image/event3/1786289891685_117422063285167014_2562150942337330825_fcc928389ee2d9d2839ff8ed69791e96.jpg)
![Event Image](/aws-image/event3/1786289891784_117422063285167014_2562150942337330825_97a297edaf0453c7e904709bd0d5b410.jpg)
![Event Image](/aws-image/event3/1786289891844_117422063285167014_2562150942337330825_64344e1f15e8cff2dbc4b526e8c0a7e0.jpg)
