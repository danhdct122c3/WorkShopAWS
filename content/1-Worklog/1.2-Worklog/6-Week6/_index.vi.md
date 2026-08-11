---
title: "Tuần 6: Tích hợp Xác thực Đa lớp (Cognito)"
date: 2026-06-22
weight: 6
chapter: false
pre: " <b> 1.2.6. </b> "
---

# Tuần 6: Tích hợp Xác thực Đa lớp (Cognito)

**Thành viên:** Backend Developer

## 1. Mục tiêu công việc
Tạo Amazon Cognito User Pool. Viết lớp middleware để chặn các API, chỉ cho phép đi qua khi có JWT Token hợp lệ.

## 2. Nhật ký công việc chi tiết

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---|---|---|
| 2 | - Thiết lập Amazon Cognito User Pool. Cấu hình các chính sách yêu cầu bảo mật (Password policy). | 27/07/2026 | 27/07/2026 | Tài liệu AWS / Github |
| 3 | - Viết script tự động đồng bộ: Thêm User mới vào DynamoDB sẽ tự tạo account trong Cognito. | 28/07/2026 | 28/07/2026 | StackOverflow |
| 4 | - Xây dựng lớp bảo vệ API (Dependency Auth). Fetch Public Keys (JWKS) từ Cognito về để lưu cache. | 29/07/2026 | 29/07/2026 | API Docs |
| 5 | - Dùng thư viện python-jose giải mã và kiểm tra Signature JWT Access Token. | 30/07/2026 | 30/07/2026 | AWS Blogs |
| 6 | - Gắn Dependency Auth vào các Endpoint. Khai báo Security Schema để test trực tiếp trên Swagger UI. | 31/07/2026 | 31/07/2026 | Báo cáo tuần |


## 3. Các kết quả đạt được
- Hoàn thành các tính năng và mục tiêu đề ra trong tuần.
- Tích hợp thành công với các dịch vụ AWS liên quan (nếu có).
- Đảm bảo chất lượng công việc đáp ứng yêu cầu của dự án.

## 4. Khó khăn & Hướng giải quyết
- **Khó khăn:** Quá trình tìm hiểu và tích hợp đôi lúc gặp lỗi không mong muốn. Cần nhiều thời gian đọc log và tài liệu kỹ thuật của AWS.
- **Giải pháp:** Phối hợp cùng các thành viên khác trong nhóm để trao đổi, đọc kỹ tài liệu hướng dẫn và tham khảo thêm ý kiến của Mentor.

## 5. Kế hoạch tuần tiếp theo
- Rà soát lại công việc của tuần này (Review).
- Bắt tay vào nghiên cứu và triển khai các nhiệm vụ của Tuần 7.
