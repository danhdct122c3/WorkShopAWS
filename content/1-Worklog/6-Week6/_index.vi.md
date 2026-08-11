---
title: "Tuần 6: Tích hợp Xác thực Đa lớp (Cognito)"
date: 2026-06-22
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

# Tuần 6: Tích hợp Xác thực Đa lớp (Cognito)

**Thành viên:** Backend Developer

## 1. Mục tiêu công việc
Tạo Amazon Cognito User Pool. Viết lớp middleware để chặn các API, chỉ cho phép đi qua khi có JWT Token hợp lệ.

## 2. Nhật ký công việc chi tiết

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---|---|---|
| 2 | - Tích hợp AWS Cognito cho luồng Auth: Gọi `admin_create_user` để tạo tài khoản.<br>- Xử lý logic Cognito tự sinh Temporary Password mà không cần email thủ công. | 27/07/2026 | 27/07/2026 | https://docs.aws.amazon.com/ |
| 3 | - Xây dựng API `respond-challenge` để xử lý trạng thái NEW_PASSWORD_REQUIRED.<br>- Thêm middleware kiểm tra JWT token và phân quyền RBAC. | 28/07/2026 | 28/07/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - Hoàn thiện API đăng nhập: Trả về JWT Access Token và Id Token cho client.<br>- Cập nhật API tự đăng ký khuôn mặt mà không cần qua Admin. | 29/07/2026 | 29/07/2026 | https://docs.aws.amazon.com/ |
| 5 | - Thêm rào chắn chống trùng lặp khuôn mặt: Gọi `SearchFacesByImage` trước khi `IndexFaces`.<br>- Phát triển tính năng đăng nhập bằng khuôn mặt trả về JWT thay thế mật khẩu. | 30/07/2026 | 30/07/2026 | https://cloudjourney.awsstudygroup.com/ |
| 6 | - Rà soát phân quyền API Backend theo RBAC: Chặn các role không hợp lệ truy cập.<br>- Khắc phục lỗi rò rỉ, tối ưu bảo mật theo 6 trụ cột AWS Well-Architected Framework. | 31/07/2026 | 31/07/2026 | https://docs.aws.amazon.com/ |



## 3. Các kết quả đạt được
- Tích hợp hoàn chỉnh AWS Cognito, bảo mật toàn bộ API bằng JWT, và hoàn thiện RBAC Backend.
