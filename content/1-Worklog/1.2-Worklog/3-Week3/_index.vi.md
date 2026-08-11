---
title: "Tuần 3: Khởi tạo FastAPI & Cơ sở dữ liệu DynamoDB"
date: 2026-06-22
weight: 3
chapter: false
pre: " <b> 1.2.3. </b> "
---

# Tuần 3: Khởi tạo FastAPI & Cơ sở dữ liệu DynamoDB

**Thành viên:** Backend Developer

## 1. Mục tiêu công việc
Khởi tạo FastAPI, cấu trúc thư mục (Router/Service). Áp dụng thiết kế lên Amazon DynamoDB và kết nối thông qua boto3.

## 2. Nhật ký công việc chi tiết

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---|---|---|
| 2 | - Khởi tạo Virtual Environment. Cài đặt các thư viện: FastAPI, Boto3. Thiết lập cấu trúc module. | 06/07/2026 | 06/07/2026 | Tài liệu AWS / Github |
| 3 | - Triển khai mô hình dữ liệu lên Amazon DynamoDB với 5 bảng chính: Users, Tasks, Leaves, Attendance, Settings. | 07/07/2026 | 07/07/2026 | StackOverflow |
| 4 | - Viết lớp Repository cấu hình Boto3 Resource. Xử lý phép chuyển đổi dữ liệu Python sang DynamoDB. | 08/07/2026 | 08/07/2026 | API Docs |
| 5 | - Định nghĩa các Pydantic Schema để kiểm tra tính hợp lệ dữ liệu đầu vào (Data Validation). | 09/07/2026 | 09/07/2026 | AWS Blogs |
| 6 | - Viết luồng API đăng ký và lấy thông tin Nhân sự (CRUD Users) theo mô hình Controller - Service. | 10/07/2026 | 10/07/2026 | Báo cáo tuần |


## 3. Các kết quả đạt được
- Hoàn thành các tính năng và mục tiêu đề ra trong tuần.
- Tích hợp thành công với các dịch vụ AWS liên quan (nếu có).
- Đảm bảo chất lượng công việc đáp ứng yêu cầu của dự án.

## 4. Khó khăn & Hướng giải quyết
- **Khó khăn:** Quá trình tìm hiểu và tích hợp đôi lúc gặp lỗi không mong muốn. Cần nhiều thời gian đọc log và tài liệu kỹ thuật của AWS.
- **Giải pháp:** Phối hợp cùng các thành viên khác trong nhóm để trao đổi, đọc kỹ tài liệu hướng dẫn và tham khảo thêm ý kiến của Mentor.

## 5. Kế hoạch tuần tiếp theo
- Rà soát lại công việc của tuần này (Review).
- Bắt tay vào nghiên cứu và triển khai các nhiệm vụ của Tuần 4.
