---
title: "Tuần 7: Phân quyền (RBAC) & API Gateway"
date: 2026-06-22
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---





## 1. Mục tiêu công việc
Cài đặt phân quyền Admin, Manager, Staff. Đóng gói mã nguồn (Mangum) và tích hợp Amazon API Gateway.

## 2. Nhật ký công việc chi tiết

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---|---|---|
| 2 | - Thiết kế bảng DynamoDB `smart-campus-leaves` với các GSI phục vụ truy vấn.<br>- Viết API tạo đơn xin nghỉ phép (Leave Request) hỗ trợ WFH, ANNUAL_LEAVE, v.v. | 03/08/2026 | 03/08/2026 | https://docs.aws.amazon.com/ |
| 3 | - Phát triển logic Backend kiểm tra chồng lấn khoảng thời gian (date_from - date_to).<br>- Chặn các đơn trùng lặp với lịch đã PENDING/APPROVED hoặc trùng ngày lễ. | 04/08/2026 | 04/08/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - Viết API xét duyệt đa cấp: Cho phép Manager/Admin duyệt hoặc từ chối đơn nghỉ phép.<br>- Phát triển API Hủy đơn dành riêng cho user, kiểm tra ràng buộc thời gian hợp lệ. | 05/08/2026 | 05/08/2026 | https://docs.aws.amazon.com/ |
| 5 | - Tích hợp logic đồng bộ tự động trạng thái điểm danh PRESENT cho ngày WFH.<br>- Bổ sung API cấu hình Quản lý Ngày lễ (Holidays) dành riêng cho role Admin. | 06/08/2026 | 06/08/2026 | https://cloudjourney.awsstudygroup.com/ |
| 6 | - Chuẩn hóa lại các enum role trong Backend (ADMIN, DIRECTOR, MANAGER, STAFF, TECHNICIAN).<br>- Thêm interceptor giới hạn quyền STAFF chỉ được tạo task loại INCIDENT. | 07/08/2026 | 07/08/2026 | https://docs.aws.amazon.com/ |



## 3. Các kết quả đạt được
- Hoàn thiện module Leave Management với logic kiểm tra chống chồng lấn phức tạp và đồng bộ sự kiện điểm danh.
