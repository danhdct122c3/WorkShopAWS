---
title: "Tuần 5: Xử lý Upload file (Presigned URL)"
date: 2026-06-22
weight: 5
chapter: false
pre: " <b> 1.2.5. </b> "
---

# Tuần 5: Xử lý Upload file (Presigned URL)

**Thành viên:** Backend Developer

## 1. Mục tiêu công việc
Xử lý bài toán upload bằng cách cấp phát Presigned URL (AWS S3) thay vì tải qua API Gateway để tránh timeout và limit dung lượng.

## 2. Nhật ký công việc chi tiết

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---|---|---|
| 2 | - Phân tích hạn chế tải file qua API Gateway (10MB limit). Lên phương án dùng S3 Presigned URL. | 20/07/2026 | 20/07/2026 | Tài liệu AWS / Github |
| 3 | - Thiết lập bucket S3 lưu trữ báo cáo. Cấu hình CORS policy để Frontend có thể upload chéo domain. | 21/07/2026 | 21/07/2026 | StackOverflow |
| 4 | - Viết API `/tasks/presigned-url` gọi hàm `generate_presigned_url` của boto3 sinh link tạm thời. | 22/07/2026 | 22/07/2026 | API Docs |
| 5 | - Tích hợp API lưu thông tin metadata của file (URL, tên file) vào bảng Tasks trên DynamoDB. | 23/07/2026 | 23/07/2026 | AWS Blogs |
| 6 | - Thiết lập Validation Content-Type chặn upload các file mã độc, hỗ trợ team debug luồng upload. | 24/07/2026 | 24/07/2026 | Báo cáo tuần |


## 3. Các kết quả đạt được
- Hoàn thành các tính năng và mục tiêu đề ra trong tuần.
- Tích hợp thành công với các dịch vụ AWS liên quan (nếu có).
- Đảm bảo chất lượng công việc đáp ứng yêu cầu của dự án.

## 4. Khó khăn & Hướng giải quyết
- **Khó khăn:** Quá trình tìm hiểu và tích hợp đôi lúc gặp lỗi không mong muốn. Cần nhiều thời gian đọc log và tài liệu kỹ thuật của AWS.
- **Giải pháp:** Phối hợp cùng các thành viên khác trong nhóm để trao đổi, đọc kỹ tài liệu hướng dẫn và tham khảo thêm ý kiến của Mentor.

## 5. Kế hoạch tuần tiếp theo
- Rà soát lại công việc của tuần này (Review).
- Bắt tay vào nghiên cứu và triển khai các nhiệm vụ của Tuần 6.
