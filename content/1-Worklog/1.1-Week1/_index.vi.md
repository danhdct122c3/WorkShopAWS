---
title: "Worklog Tuần 1"
date: 2026-06-22
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

### Mục tiêu tuần 1:

* Làm quen với môi trường và chương trình thực tập tại FCAJ.
* Nắm vững các khái niệm nền tảng về điện toán đám mây và hệ sinh thái AWS.
* Thực hành thiết lập tài khoản, công cụ dòng lệnh và môi trường phát triển.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|-----|-----------|--------------|-----------------|----------------|
| 2 | - Tìm hiểu quy định, lộ trình và yêu cầu của chương trình thực tập tại FCAJ. <br> - Đọc và lưu ý các nội quy, quy định tại đơn vị thực tập. <br> - Đọc tài liệu hướng dẫn về tiêu chí đánh giá project. <br> - Tìm hiểu các yêu cầu bắt buộc như báo cáo, blog, sơ đồ kiến trúc và số lượng dịch vụ AWS cần sử dụng. <br> - Xác định định hướng xây dựng ứng dụng thực tế trên nền tảng AWS. | 22/06/2026 | 22/06/2026 | https://hcm-rules.awsfcaj.com/ |
| 3 | - Tìm hiểu các khái niệm cơ bản về điện toán đám mây: Cloud Computing là gì, lợi ích và các mô hình dịch vụ (IaaS, PaaS, SaaS). <br> - Tìm hiểu sự khác biệt giữa on-premises và cloud. <br> - Nghiên cứu về AWS Global Infrastructure: Region, Availability Zone (AZ), Edge Location. <br> - Tìm hiểu sự khác nhau giữa các dịch vụ global (IAM, Route 53) và các dịch vụ regional (EC2, S3). <br> - Tạo AWS Free Tier account. <br> - Làm quen với AWS Management Console. | 23/06/2026 | 23/06/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - Tìm hiểu AWS Identity and Access Management (IAM): Users, Groups, Roles, Policies. <br> - Tìm hiểu nguyên tắc Least Privilege và tầm quan trọng trong bảo mật. <br> - Nghiên cứu cấu trúc cơ bản của một IAM Policy (JSON). <br> - Tìm hiểu AWS Billing Dashboard, AWS Budgets và Cost Explorer. <br> **Thực hành:** <br>&emsp; + Cài đặt AWS CLI và cấu hình (Access Key, Secret Key, Region). <br>&emsp; + Truy cập IAM Dashboard, quan sát cấu trúc User, Role, Policy. <br>&emsp; + Tạo IAM User mới, gán quyền và thực hành đăng nhập. | 24/06/2026 | 24/06/2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | - Tìm hiểu các nhóm dịch vụ chính của AWS: <br>&emsp; + **Compute:** EC2, Lambda, ECS, Fargate. <br>&emsp; + **Storage:** S3 (Object Storage), EBS (Block Storage). <br>&emsp; + **Database:** DynamoDB (NoSQL), RDS (SQL), ElastiCache. <br>&emsp; + **Networking:** VPC, API Gateway, CloudFront, Route 53. <br>&emsp; + **Monitoring:** CloudWatch, AWS X-Ray. <br> - Tìm hiểu mô hình triển khai truyền thống (VM-based) so với Serverless. <br> **Thực hành:** <br>&emsp; + Tạo thử S3 Bucket và upload file. <br>&emsp; + Khám phá giao diện Lambda, DynamoDB, EC2 Console. | 25/06/2026 | 25/06/2026 | https://cloudjourney.awsstudygroup.com/ |
| 6 | - Nghiên cứu chuyên sâu kiến trúc **Serverless**: Không cần quản lý server, tự động scale, mô hình tính phí theo lần gọi. <br> - Nghiên cứu kiến trúc **Event-Driven Architecture**: Publish/Subscribe, Point-to-Point, Streaming. <br> - Tìm hiểu về Amazon EventBridge: Event Bus, Rules, Targets. <br> - Tìm hiểu về Amazon API Gateway: REST API, Lambda Integration, Stage. <br> - Đọc tài liệu về AWS Lambda: Handler, Trigger, Environment Variables, Timeout, Memory. <br> **Thực hành:** <br>&emsp; + Tạo một hàm Lambda "Hello World" đơn giản. <br>&emsp; + Cấu hình API Gateway trigger gọi Lambda và test bằng curl/Postman. | 27/06/2026 | 27/06/2026 | https://cloudjourney.awsstudygroup.com/ |

### Kết quả đạt được tuần 1:

* Hiểu được điện toán đám mây là gì và tại sao nên sử dụng AWS thay vì on-premises.
* Nắm vững cấu trúc AWS Global Infrastructure (Region, AZ, Edge Location) và lý do thiết kế nhiều tầng đó.
* Tạo và cấu hình thành công AWS Free Tier account, hiểu về các giới hạn Free Tier để tránh chi phí phát sinh.
* Thiết lập AWS CLI thành công với đầy đủ thông tin:
  * Access Key / Secret Key
  * Default Region (ap-southeast-1 - Singapore)
  * Output format (json)
* Hiểu được IAM và áp dụng nguyên tắc Least Privilege: chỉ cấp quyền tối thiểu cần thiết.
* Phân biệt được các nhóm dịch vụ AWS và biết khi nào dùng dịch vụ nào:
  * Lambda thay vì EC2 khi không cần quản lý server
  * DynamoDB thay vì RDS khi cần NoSQL linh hoạt và scale cao
  * S3 khi cần lưu trữ file/object
* Nắm vững kiến trúc Event-Driven: hiểu cách các dịch vụ giao tiếp với nhau qua Events thay vì gọi trực tiếp.
* Tạo thành công một hàm Lambda đơn giản và kết nối với API Gateway để tạo REST endpoint đầu tiên.
