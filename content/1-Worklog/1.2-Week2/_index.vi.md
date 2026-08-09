---
title: "Worklog Tuần 2"
date: 2026-06-30
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Mục tiêu tuần 2:

* Phân tích bài toán thực tế và xác định rõ nghiệp vụ cho dự án Smart Campus.
* Nghiên cứu chuyên sâu các dịch vụ AWS sẽ sử dụng trong dự án.
* Thiết kế kiến trúc hệ thống, cơ sở dữ liệu và lên kế hoạch phát triển chi tiết.
* Khởi tạo môi trường dự án và thiết lập hạ tầng AWS cơ bản.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|-----|-----------|--------------|-----------------|----------------|
| 2 | - Phân tích bài toán: Xây dựng hệ thống **quản lý công việc và điểm danh** cho nhân viên (Smart Campus Platform). <br> - Xác định các actor (nhân viên, quản lý, kỹ thuật viên, admin) và use-cases. <br> - Nghiên cứu Amazon DynamoDB: NoSQL, Single Table Design, Partition Key, Sort Key, GSI. <br> - Nghiên cứu Amazon Rekognition: IndexFaces, SearchFacesByImage, Collection. <br> - Nghiên cứu Amazon SNS: Topics, Subscriptions, Email/SMS notification. | 30/06/2026 | 30/06/2026 | https://docs.aws.amazon.com/ |
| 3 | - Nghiên cứu Amazon EventBridge: Event Bus, Rules-based routing, Schema Registry. <br> - Nghiên cứu Amazon S3: Bucket Policy, Presigned URL, Block Public Access. <br> - Nghiên cứu Amazon Athena + AWS Glue: Data Lake, Crawler, truy vấn S3 bằng SQL. <br> - Nghiên cứu Amazon Bedrock: Foundation Models, Invoke API, RAG architecture. <br> - Nghiên cứu Amazon CloudWatch: Metrics, Logs, Alarms, Dashboards. | 01/07/2026 | 01/07/2026 | https://docs.aws.amazon.com/ |
| 4 | - Thiết kế kiến trúc tổng thể hệ thống: Event-Driven Serverless trên AWS. <br> - Thiết kế cấu trúc Monorepo: Backend (FastAPI/Python) + Frontend (React + Vite). <br> - Định nghĩa **8 Luồng nghiệp vụ (Workflows)** cốt lõi: <br>&emsp; + WF1: Authentication (Cognito JWT) <br>&emsp; + WF2: Face Registration (Rekognition IndexFaces) <br>&emsp; + WF3: Attendance (SearchFacesByImage + Rule Engine) <br>&emsp; + WF4: Notification (SNS Multi-channel) <br>&emsp; + WF5: Analytics (DynamoDB + Athena) <br>&emsp; + WF6: AI Assistant (Bedrock NL2SQL) <br>&emsp; + WF7: Security Monitoring <br>&emsp; + WF8: Task & Employee Management | 02/07/2026 | 02/07/2026 | Thiết kế hệ thống nội bộ |
| 5 | - Thiết kế cơ sở dữ liệu DynamoDB gồm **5 bảng chính**: <br>&emsp; + `smart-campus-users`: Quản lý nhân sự (PK: user_id, GSI: email-index, role-index) <br>&emsp; + `smart-campus-faces`: Thông tin khuôn mặt đã đăng ký (PK: face_id) <br>&emsp; + `smart-campus-attendance`: Bản ghi điểm danh (PK: attendance_id, GSI: date-index, userid-index) <br>&emsp; + `smart-campus-notifications`: Lịch sử thông báo (PK: notification_id, GSI: user_id-sent_at-index) <br>&emsp; + `smart-campus-tasks`: Công việc & sự cố (PK: task_id, GSI: assigneeId-status-index) <br> - Biên soạn tài liệu kiến trúc `System_Overview_and_Task_Management.md`. | 03/07/2026 | 03/07/2026 | Thiết kế hệ thống nội bộ |
| 6 | - Khởi tạo cấu trúc thư mục dự án (Monorepo): `backend/`, `frontend/`, `docs/`. <br> - Cài đặt môi trường phát triển: Python 3.11+, Node.js 18+, FastAPI, React + Vite. <br> - Tạo thủ công 5 bảng DynamoDB trên AWS Console, cấu hình PK/SK/GSI. <br> - Cấu hình AWS CLI kết nối tài khoản thực (Access Key, Region `ap-southeast-1`). <br> - Khởi tạo S3 Bucket `smart-campus-images` để chuẩn bị lưu ảnh. <br> - Thiết lập Rekognition Collection `smart-campus-faces`. | 04/07/2026 | 04/07/2026 | https://docs.aws.amazon.com/ |

### Kết quả đạt được tuần 2:

* Phân tích rõ ràng bài toán Smart Campus với 5 loại actor và đầy đủ use-cases tương ứng.
* Hiểu chuyên sâu các dịch vụ AWS sẽ sử dụng trong dự án:
  * **DynamoDB**: Thiết kế Single Table Design, hiểu khi nào cần GSI để tối ưu truy vấn.
  * **Rekognition**: Hiểu Collection là gì và sự khác biệt giữa `IndexFaces` (đăng ký) và `SearchFacesByImage` (nhận diện).
  * **EventBridge**: Hiểu cách định tuyến Event đến nhiều target khác nhau (Lambda, SQS, SNS).
  * **Athena + Glue**: Hiểu kiến trúc Data Lake và cách truy vấn dữ liệu S3 bằng SQL.
* Hoàn tất thiết kế kiến trúc 8 Workflow cốt lõi, xác định rõ dịch vụ AWS sử dụng cho từng workflow.
* Tạo thành công 5 bảng DynamoDB trên AWS Console với đúng Partition Key, Sort Key và các Global Secondary Index cần thiết.
* Khởi tạo môi trường phát triển đầy đủ: backend FastAPI và frontend React đều chạy được trên local.
* Tài liệu kiến trúc `System_Overview_and_Task_Management.md` đã hoàn chỉnh, là cơ sở tham chiếu cho toàn bộ quá trình phát triển.
