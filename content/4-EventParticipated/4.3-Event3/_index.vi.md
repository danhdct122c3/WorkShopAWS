---
title: "Agent Forge HCMC Workshop"
date: 2026-08-09
weight: 3
chapter: false
pre: " <b> 4.3. </b> "
---

# BÀI BÁO CÁO THU HOẠCH SỰ KIỆN "AGENT FORGE HCMC WORKSHOP"

### Mục Đích Của Sự Kiện

- Cung cấp kiến thức nền tảng và chuyên sâu về Agentic AI, sự chuyển dịch từ các mô hình ngôn ngữ tĩnh (LLMs) sang các Tác tử tự trị (AI Agents) có khả năng suy luận và tự động thực thi tác vụ.
- Hướng dẫn thực hành trực tiếp (Hands-on) quy trình xây dựng AI Agent trên hạ tầng AWS thông qua các công cụ hiện đại như Kiro và framework AgentCore.
- Trang bị kỹ năng tích hợp hệ thống AI vào các luồng nghiệp vụ thực tế của doanh nghiệp (ví dụ: tự động hóa quy trình xử lý hoàn tiền), từ khâu thiết lập bộ nhớ, kết nối cơ sở dữ liệu tri thức đến việc xây dựng giao diện và bảo mật phân quyền.

### Danh Sách Diễn Giả

- **Anh Nghĩa** – Đại diện từ AWS Study Group (Trình bày phần Lý thuyết / Theory chuyên sâu về kiến trúc Agent Core, Runtime, Identity và Gateway).
- **Anh Hải Anh** – Đại diện hướng dẫn phần Thực hành (Hands-on Labs / Application).

## PHẦN 1: CƠ SỞ LÝ THUYẾT VỀ AGENTIC AI & KIẾN TRÚC HỆ THỐNG (70%)

Trong bối cảnh công nghệ thay đổi nhanh chóng, các Hệ thống Trí tuệ Nhân tạo đang dịch chuyển mạnh mẽ từ mô hình ngôn ngữ tĩnh (LLMs) sang các Tác tử tự trị (AI Agents). Workshop đã cung cấp một bức tranh lý thuyết chuyên sâu về kiến trúc và cách thức vận hành của các Agent này.

### 1. Sự tiến hóa từ LLMs sang Agentic Workflow

* **Hạn chế của LLMs truyền thống:** Các LLM (như GPT, Claude) về bản chất chỉ là những cỗ máy dự đoán từ tiếp theo dựa trên dữ liệu đã được huấn luyện. Chúng thụ động, thiếu ngữ cảnh thời gian thực và không thể tự thực thi hành động (Actionless).
* **Sức mạnh của AI Agent:** Agent là một thực thể AI có khả năng nhận thức môi trường (Perception), suy luận logic (Reasoning/Chain-of-Thought), lập kế hoạch (Planning) và sử dụng công cụ (Tool Use) để tác động ngược lại môi trường. Một Agentic Workflow cho phép AI tự động chia nhỏ một bài toán phức tạp (Task Decomposition), thực thi từng bước, tự đánh giá kết quả và sửa lỗi (Self-reflection) cho đến khi hoàn thành mục tiêu.

### 2. Ba trụ cột kiến trúc cốt lõi của một AI Agent

Sự kiện đi sâu vào mổ xẻ kiến trúc bên trong của một AI Agent tiêu chuẩn dùng trong doanh nghiệp:

* **The Brain (Não bộ - LLM):** Đóng vai trò là trung tâm phân tích. Nó tiếp nhận Prompt, xác định ý định của người dùng (Intent Recognition) và quyết định công cụ nào cần được gọi.
* **Memory (Bộ nhớ):**
  * *Short-term Memory:* Lưu trữ ngữ cảnh của phiên giao tiếp hiện tại (Session Context).
  * *Persistent / Long-term Memory:* Lưu trữ thông tin xuyên suốt các phiên làm việc (như lịch sử mua hàng, sở thích người dùng). Cơ chế này thường được triển khai thông qua các cơ sở dữ liệu Vector hoặc NoSQL (như DynamoDB) để Agent có thể truy xuất lại ngữ cảnh cũ.

* **Tools & Knowledge (Công cụ & Tri thức):**
  * *Tri thức (RAG - Retrieval-Augmented Generation):* Kỹ thuật kết nối Agent với cơ sở dữ liệu tri thức của riêng doanh nghiệp, giúp AI trả lời dựa trên dữ liệu nội bộ thay vì dữ liệu pre-train, giảm thiểu hiện tượng "ảo giác" (Hallucination).
  * *Công cụ (Tools/APIs):* Các hàm (Functions) được lập trình sẵn để Agent gọi (ví dụ: API tra cứu mã vận đơn, API thực hiện lệnh hoàn tiền).

### 3. Vận hành và Quản trị AI an toàn (Governance & Observability)

Đưa AI vào môi trường doanh nghiệp yêu cầu khắt khe về bảo mật và kiểm soát:

* **AgentCore Policies / Guardrails:** Là các bộ quy tắc (Rules) mã hóa cứng (Hard-coded) hoặc dùng Prompt Engineering nhằm thiết lập "hàng rào" giới hạn quyền lực của AI. (Ví dụ: Agent chỉ được phép đề xuất hoàn tiền nếu đơn hàng chưa quá 30 ngày, nếu không phải chuyển cho tư vấn viên con người).
* **Observability (Khả năng quan sát):** Việc theo dõi cách AI "suy nghĩ" (Reasoning Traces) là bắt buộc. Hệ thống phải ghi log chi tiết từng bước lập luận, API nào đã được gọi và payload gửi đi là gì, nhằm mục đích Audit và Debug khi hệ thống gặp lỗi.

---

## PHẦN 2: THỰC HÀNH TRIỂN KHAI VỚI KIRO & AGENTCORE (30%)

Từ nền tảng lý thuyết trên, phần thực hành (Labs) tập trung vào việc hiện thực hóa các khái niệm bằng hệ sinh thái công cụ của AWS, cụ thể là Kiro và AgentCore framework.

### 1. Khởi tạo và Định hướng Tác tử (Setup & Steering)

* Quá trình thực hành bắt đầu bằng việc thiết lập môi trường AWS Hosted Event DCV để đảm bảo tính nhất quán về cơ sở hạ tầng.
* Trọng tâm của Lab 1 là kỹ thuật **Setup Steering** trong Kiro. Đây là bước hiện thực hóa phần lý thuyết "The Brain", nơi lập trình viên viết các System Prompts và định nghĩa rõ ràng Persona (nhân cách), ranh giới nghiệp vụ, và định dạng Output chuẩn cho Agent.

### 2. Xây dựng AI Agent nghiệp vụ (Returns & Refunds Use-case)

Lab 2 áp dụng mô hình Agentic Workflow vào bài toán tự động hóa quy trình Đổi trả/Hoàn tiền (Returns & Refunds).

* **Khởi tạo nhanh:** Framework AgentCore cho phép đóng gói hạ tầng (IaC) và deploy một Agent cơ bản chỉ với 3 dòng lệnh, minh chứng cho sự tối ưu hóa quy trình DevOps đối với các ứng dụng AI.
* **Hiện thực hóa Memory & Knowledge:**
  * Tích hợp Persistent Memory bằng cách kết nối Agent với cơ sở dữ liệu Amazon DynamoDB. Điều này cho phép Agent truy vấn trạng thái thực của các đơn hàng (Real Data Connection) để quyết định xem có đủ điều kiện hoàn tiền hay không.

* **Bảo mật & Tương tác:**
  * Triển khai giao diện người dùng bằng Streamlit Chat UI, kết hợp Amazon Cognito để cấp quyền truy cập (Authentication), đảm bảo chỉ những người dùng hợp lệ mới được chat với hệ thống.
  * Kích hoạt các Policies (như đã học ở phần lý thuyết) để ngăn chặn Agent tự ý hoàn tiền vượt hạn mức, đồng thời cấu hình Observability để theo dõi luồng gọi API nội bộ của tác tử.

---

## PHẦN 3: BÀI HỌC VÀ ĐỊNH HƯỚNG ỨNG DỤNG CÁ NHÂN

Thông qua việc kết nối giữa lý thuyết hệ thống tự trị và thực hành trên AWS, kiến trúc AgentCore mở ra nhiều hướng ứng dụng mạnh mẽ cho việc phát triển phần mềm hiện đại:

* **Tích hợp AI vào kiến trúc Microservices:** Khi thiết kế các hệ thống Backend (ví dụ hệ thống Booking hoặc E-commerce), thay vì xử lý mọi logic bằng code tuần tự cứng nhắc, tôi có thể đóng gói AI Agent thành một service độc lập. Service này sẽ giao tiếp với các services khác (như Product Service, Payment Service) thông qua RESTful API hoặc qua event streaming (Apache Kafka) để xử lý các nghiệp vụ động, có tính phân tích cao.
* **Tối ưu thiết kế cơ sở dữ liệu cho AI:** Việc thực hành với DynamoDB giúp củng cố tư duy thiết kế cơ sở dữ liệu phi quan hệ (NoSQL) lưu trữ ngữ cảnh (Memory) và lịch sử giao tiếp, vốn là một thành phần bắt buộc khi thiết kế API cho AI chatbots.
* **Phát triển kỹ năng Vibe Coding & DevOps:** Sử dụng các công cụ như Kiro hoặc AgentCore Harness giúp làm quen với tư duy dùng AI để sinh code, viết test và tự động hóa khâu triển khai CI/CD, từ đó tối ưu hóa vòng đời phát triển phần mềm trong giai đoạn chuẩn bị bước vào các môi trường doanh nghiệp thực tế.

#### Một số hình ảnh khi tham gia sự kiện

![Event Image](/aws-image/event3/1786289891441_117422063285167014_2562150942337330825_6e6dda0b3cf7a1ddcaf9ec5689d98f01.jpg)
![Event Image](/aws-image/event3/1786289891501_117422063285167014_2562150942337330825_ed14ca293fbccdc28a4a3f81200354ea.jpg)
![Event Image](/aws-image/event3/1786289891555_117422063285167014_2562150942337330825_cecde5dea800915f41004d0fdb63679f.jpg)
![Event Image](/aws-image/event3/1786289891630_117422063285167014_2562150942337330825_47d4f3fb640da05dc5dfca20cabfba67.jpg)
![Event Image](/aws-image/event3/1786289891685_117422063285167014_2562150942337330825_fcc928389ee2d9d2839ff8ed69791e96.jpg)
![Event Image](/aws-image/event3/1786289891784_117422063285167014_2562150942337330825_97a297edaf0453c7e904709bd0d5b410.jpg)
![Event Image](/aws-image/event3/1786289891844_117422063285167014_2562150942337330825_64344e1f15e8cff2dbc4b526e8c0a7e0.jpg)

