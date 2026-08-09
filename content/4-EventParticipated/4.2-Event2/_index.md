---
title: "FCAJ x Agentic AI Build Week"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 4.2. </b> "
---

### Event Objectives

- Share best practices in modern application design
- Introduce Domain-Driven Design (DDD) and event-driven architecture
- Provide guidance on selecting the right compute services
- Present AI tools to support the development lifecycle

### Speakers

- **Jignesh Shah** – Director, Open Source Databases
- **Erica Liu** – Sr. GTM Specialist, AppMod
- **Fabrianne Effendi** – Assc. Specialist SA, Serverless Amazon Web Services

### Key Highlights

#### Identifying the drawbacks of legacy application architecture

- Long product release cycles → Lost revenue/missed opportunities  
- Inefficient operations → Reduced productivity, higher costs  
- Non-compliance with security regulations → Security breaches, loss of reputation  

#### Transitioning to modern application architecture – Microservices

Migrating to a modular system — each function is an **independent service** communicating via **events**, built on three core pillars:

- **Queue Management**: Handle asynchronous tasks  
- **Caching Strategy**: Optimize performance  
- **Message Handling**: Flexible inter-service communication  

#### Domain-Driven Design (DDD)

- **Four-step method**: Identify domain events → arrange timeline → identify actors → define bounded contexts  
- **Bookstore case study**: Demonstrates real-world DDD application  
- **Context mapping**: 7 patterns for integrating bounded contexts  

#### Event-Driven Architecture

- **3 integration patterns**: Publish/Subscribe, Point-to-point, Streaming  
- **Benefits**: Loose coupling, scalability, resilience  
- **Sync vs async comparison**: Understanding the trade-offs  

#### Compute Evolution

- **Shared Responsibility Model**: EC2 → ECS → Fargate → Lambda  
- **Serverless benefits**: No server management, auto-scaling, pay-for-value  
- **Functions vs Containers**: Criteria for appropriate choice  

#### Amazon Q Developer

- **SDLC automation**: From planning to maintenance  
- **Code transformation**: Java upgrade, .NET modernization  
- **AWS Transform agents**: VMware, Mainframe, .NET migration  

### Key Takeaways

#### Design Mindset

- **Business-first approach**: Always start from the business domain, not the technology  
- **Ubiquitous language**: Importance of a shared vocabulary between business and tech teams  
- **Bounded contexts**: Identifying and managing complexity in large systems  

#### Technical Architecture

- **Event storming technique**: Practical method for modeling business processes  
- Use **event-driven communication** instead of synchronous calls  
- **Integration patterns**: When to use sync, async, pub/sub, streaming  
- **Compute spectrum**: Criteria for choosing between VM, containers, and serverless  

#### Modernization Strategy

- **Phased approach**: No rushing — follow a clear roadmap  
- **7Rs framework**: Multiple modernization paths depending on the application  
- **ROI measurement**: Cost reduction + business agility  

### Applying to Work

- **Apply DDD** to current projects: Event storming sessions with business teams  
- **Refactor microservices**: Use bounded contexts to define service boundaries  
- **Implement event-driven patterns**: Replace some sync calls with async messaging  
- **Adopt serverless**: Pilot AWS Lambda for suitable use cases  
- **Try Amazon Q Developer**: Integrate into the dev workflow to boost productivity  

### Event Experience

Attending the **“GenAI-powered App-DB Modernization”** workshop was extremely valuable, giving me a comprehensive view of modernizing applications and databases using advanced methods and tools. Key experiences included:

#### Learning from highly skilled speakers
- Experts from AWS and major tech organizations shared **best practices** in modern application design.  
- Through real-world case studies, I gained a deeper understanding of applying **DDD** and **Event-Driven Architecture** to large projects.  

#### Hands-on technical exposure
- Participating in **event storming** sessions helped me visualize how to **model business processes** into domain events.  
- Learned how to **split microservices** and define **bounded contexts** to manage large-system complexity.  
- Understood trade-offs between **synchronous and asynchronous communication** and integration patterns like **pub/sub, point-to-point, streaming**.  

#### Leveraging modern tools
- Explored **Amazon Q Developer**, an AI tool for SDLC support from planning to maintenance.  
- Learned to **automate code transformation** and pilot serverless with **AWS Lambda** to improve productivity.  

#### Networking and discussions
- The workshop offered opportunities to exchange ideas with experts, peers, and business teams, enhancing the **ubiquitous language** between business and tech.  
- Real-world examples reinforced the importance of the **business-first approach** rather than focusing solely on technology.  

#### Lessons learned
- Applying DDD and event-driven patterns reduces **coupling** while improving **scalability** and **resilience**.  
- Modernization requires a **phased approach** with **ROI measurement**; rushing the process can be risky.  
- AI tools like Amazon Q Developer can significantly **boost productivity** when integrated into the current workflow.  

#### Some event photos
![Event Image](/aws-image/event2/1786289938790_117422063285167014_2562150942337330825_9826e7c9a37b676323df79073c35f939.jpg)
![Event Image](/aws-image/event2/1786289938835_117422063285167014_2562150942337330825_4f4d73c4900292562860a738bf838f34.jpg)
![Event Image](/aws-image/event2/1786289938886_117422063285167014_2562150942337330825_f31f05388391f8db149333b205272b9a.jpg)
![Event Image](/aws-image/event2/1786289938950_117422063285167014_2562150942337330825_aa208e1157edaa727ef3eb8dcb5d6503.jpg)
![Event Image](/aws-image/event2/1786289939015_117422063285167014_2562150942337330825_91e91e50a5fe62040b33a0866470ba77.jpg)
![Event Image](/aws-image/event2/1786289939060_117422063285167014_2562150942337330825_aa6bbb8de3ecfd430ed8bf6499c88a84.jpg)
![Event Image](/aws-image/event2/1786289939143_117422063285167014_2562150942337330825_17e5ab30a97259d4f393a1aa8733dea6.jpg)
![Event Image](/aws-image/event2/1786289939203_117422063285167014_2562150942337330825_1757a1a86f6ee9b9dc4b0757e8d4e8de.jpg)
![Event Image](/aws-image/event2/1786289939250_117422063285167014_2562150942337330825_1be42adc6efe5edfea1a97b928456c61.jpg)  

> Overall, the event not only provided technical knowledge but also helped me reshape my thinking about application design, system modernization, and cross-team collaboration.
