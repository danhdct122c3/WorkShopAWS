---
title: "Tuần 4: Xây dựng Core API & Rule Engine"
date: 2026-06-22
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

# Tuần 4: Xây dựng Core API & Rule Engine

**Thành viên:** Backend Developer

## 1. Mục tiêu công việc
Hoàn thành CRUD cho Users, Tasks. Viết Rule Engine tính toán logic Điểm danh trễ/đúng giờ dựa trên bảng Settings.

## 2. Nhật ký công việc chi tiết

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---|---|---|
| 2 | - Viết API CRUD Quản lý công việc và Đơn từ. Sử dụng GSI truy vấn danh sách theo mã nhân viên. | 13/07/2026 | 13/07/2026 | Tài liệu AWS / Github |
| 3 | - Áp dụng kỹ thuật Denormalization trên DynamoDB để tránh JOIN bảng, giảm thời gian phản hồi. | 14/07/2026 | 14/07/2026 | StackOverflow |
| 4 | - Viết API nhận log điểm danh (đã qua nhận diện AI) từ frontend truyền xuống. | 15/07/2026 | 15/07/2026 | API Docs |
| 5 | - Xây dựng Rule Engine Điểm danh: Query giờ làm việc chuẩn để gán trạng thái PRESENT hoặc LATE. | 16/07/2026 | 16/07/2026 | AWS Blogs |
| 6 | - Mở rộng Rule Engine xử lý Early Leave và viết Unit Test cho khối logic bằng Pytest. | 17/07/2026 | 17/07/2026 | Báo cáo tuần |


## 3. Các kết quả đạt được
- Hoàn thành các tính năng và mục tiêu đề ra trong tuần.
- Tích hợp thành công với các dịch vụ AWS liên quan (nếu có).
- Đảm bảo chất lượng công việc đáp ứng yêu cầu của dự án.

## 4. Khó khăn & Hướng giải quyết
- **Khó khăn:** Quá trình tìm hiểu và tích hợp đôi lúc gặp lỗi không mong muốn. Cần nhiều thời gian đọc log và tài liệu kỹ thuật của AWS.
- **Giải pháp:** Phối hợp cùng các thành viên khác trong nhóm để trao đổi, đọc kỹ tài liệu hướng dẫn và tham khảo thêm ý kiến của Mentor.

## 5. Kế hoạch tuần tiếp theo
- Rà soát lại công việc của tuần này (Review).
- Bắt tay vào nghiên cứu và triển khai các nhiệm vụ của Tuần 5.
