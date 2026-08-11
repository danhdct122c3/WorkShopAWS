---
title: "Tuần 7: Phân quyền (RBAC) & API Gateway"
date: 2026-06-22
weight: 7
chapter: false
pre: " <b> 1.2.7. </b> "
---

# Tuần 7: Phân quyền (RBAC) & API Gateway

**Thành viên:** Backend Developer

## 1. Mục tiêu công việc
Cài đặt phân quyền Admin, Manager, Staff. Đóng gói mã nguồn (Mangum) và tích hợp Amazon API Gateway.

## 2. Nhật ký công việc chi tiết

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---|---|---|
| 2 | - Thiết kế Role-Based Access Control (RBAC). Viết hàm kiểm tra quyền nâng cao (Authorization Decorator). | 03/08/2026 | 03/08/2026 | Tài liệu AWS / Github |
| 3 | - Phát triển logic phân quyền nghiệp vụ: Duyệt đơn từ theo phòng ban, bảo mật thông tin cá nhân. | 04/08/2026 | 04/08/2026 | StackOverflow |
| 4 | - Cài đặt thư viện Mangum. Bọc app FastAPI bằng Mangum để chạy trên môi trường Serverless. | 05/08/2026 | 05/08/2026 | API Docs |
| 5 | - Thiết lập Lambda Function (Memory, Timeout) và cấu hình Amazon API Gateway (HTTP API). | 06/08/2026 | 06/08/2026 | AWS Blogs |
| 6 | - Dọn dẹp code rác, cập nhật `requirements.txt`. Hỗ trợ DevOps viết pytest để chạy trong CI/CD. | 07/08/2026 | 07/08/2026 | Báo cáo tuần |


## 3. Các kết quả đạt được
- Hoàn thành các tính năng và mục tiêu đề ra trong tuần.
- Tích hợp thành công với các dịch vụ AWS liên quan (nếu có).
- Đảm bảo chất lượng công việc đáp ứng yêu cầu của dự án.

## 4. Khó khăn & Hướng giải quyết
- **Khó khăn:** Quá trình tìm hiểu và tích hợp đôi lúc gặp lỗi không mong muốn. Cần nhiều thời gian đọc log và tài liệu kỹ thuật của AWS.
- **Giải pháp:** Phối hợp cùng các thành viên khác trong nhóm để trao đổi, đọc kỹ tài liệu hướng dẫn và tham khảo thêm ý kiến của Mentor.

## 5. Kế hoạch tuần tiếp theo
- Rà soát lại công việc của tuần này (Review).
- Bắt tay vào nghiên cứu và triển khai các nhiệm vụ của Tuần 8.
