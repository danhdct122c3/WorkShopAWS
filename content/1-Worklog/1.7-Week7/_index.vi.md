---
title: "Worklog Tuần 7"
date: 2026-08-04
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu tuần 7:

* Thiết kế và xây dựng hoàn chỉnh module Quản lý Nghỉ phép (Leave Management) với lịch tương tác và logic nghiệp vụ phức tạp.
* Nâng cấp trải nghiệm người dùng với Toast Notification in-house và chuẩn hóa phân quyền hệ thống.
* Hoàn thiện luồng Check-out điểm danh và điểm danh WFH.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|-----|-----------|--------------|-----------------|----------------|
| 2 | - Thiết kế DynamoDB Table `smart-campus-leaves`: Khởi tạo bảng lưu đơn xin nghỉ với GSI `user_id-index` và `status-index`. <br> - Phát triển Backend Module `leaves`: <br>&emsp; + 4 loại nghỉ phép: `WFH` (Làm việc từ xa), `ANNUAL_LEAVE` (Phép năm), `SICK_LEAVE` (Nghỉ ốm), `BUSINESS_TRIP` (Công tác). <br>&emsp; + Luồng duyệt đa cấp: Nhân viên nộp đơn → Quản lý duyệt/từ chối. <br>&emsp; + API quản lý Ngày lễ (Holidays): Admin thiết lập danh sách ngày lễ trong năm. | 04/08/2026 | 04/08/2026 | DynamoDB Docs |
| 3 | - Xây dựng **Logic chống trùng lịch** (Backend): <br>&emsp; + Kiểm tra khoảng thời gian `date_from – date_to` với các đơn cũ (PENDING/APPROVED). <br>&emsp; + Chặn và báo lỗi nếu xin nghỉ trùng lịch. <br> - **Ràng buộc Ngày lễ**: Backend tự động quét date range → Chặn nếu trùng với Ngày lễ Admin đã cấu hình. <br> - Phát triển tính năng **Hủy đơn** (`PATCH /leaves/{id}/cancel`): <br>&emsp; + Chỉ hủy được khi đơn ở trạng thái `PENDING` hoặc `APPROVED`. <br>&emsp; + Không hủy đơn trong quá khứ hoặc đã đến ngày bắt đầu. | 05/08/2026 | 05/08/2026 | FastAPI Docs |
| 4 | - Xây dựng trang `Leaves.jsx` (Frontend): <br>&emsp; + **Interactive Calendar**: Lưới lịch trực quan, đổ màu theo trạng thái (Ngày lễ, Nghỉ phép, WFH, Cuối tuần). <br>&emsp; + **Form Đăng ký Thông minh**: Tự động điền ngày được chọn trên lịch. <br>&emsp; + **Tích hợp Điểm danh WFH**: Nhân sự được duyệt WFH có nút "Check-in WFH", tự động đồng bộ kết quả `PRESENT` sang module Attendance. <br>&emsp; + Nút **"Hủy"** màu đỏ cho các đơn đủ điều kiện hủy. <br>&emsp; + Badge `Đã hủy` màu xám mờ phân biệt với `Từ chối`. | 06/08/2026 | 06/08/2026 | React Docs |
| 5 | - Nâng cấp UX – **Toast Notification Component in-house** (thay thế `alert()` xấu xí): <br>&emsp; + Glassmorphism style (backdrop blur, transparent, border gradient). <br>&emsp; + Animation `fadeInDown`: Xuất hiện từ trên rơi xuống. <br>&emsp; + Tự động mờ và biến mất sau 4 giây. <br>&emsp; + Hỗ trợ 2 kiểu: Lỗi (màu đỏ) và Thành công (màu xanh). <br> - Áp dụng Toast Notification cho toàn bộ module `Leaves.jsx` thay thế mọi `alert()`. <br> - Phân trang cục bộ cho trang Notifications (10 mục/trang), tái sử dụng Hybrid Chunk Pagination. | 07/08/2026 | 07/08/2026 | CSS Animation Docs |
| 6 | - **Chuẩn hóa Roles**: Lược bỏ role dư thừa, cấu trúc lại 5 roles tinh gọn: `ADMIN`, `DIRECTOR`, `MANAGER`, `STAFF`, `TECHNICIAN`. <br> - **Chuẩn hóa Departments**: Đổi `MAINTENANCE` → `TECHNICAL`. Mở quyền DIRECTOR quản lý Users và WAF. Giới hạn STAFF chỉ tạo task INCIDENT. <br> - Fix bug 500 Backend: Script migration cập nhật DynamoDB đồng bộ role/department cũ theo định nghĩa mới. <br> - Hoàn thiện luồng **Check-out điểm danh**: Khung giờ hợp lệ `8h30–9h30` (Check-in) và `17h30–18h30` (Check-out). <br> - Fix thời gian Check-in WFH: Ghi nhận thời gian thực thay vì hardcode `07:00:00`. | 08/08/2026 | 08/08/2026 | DynamoDB Docs |

### Kết quả đạt được tuần 7:

* Module Leave Management hoàn chỉnh với đầy đủ nghiệp vụ:
  * 4 loại nghỉ phép, luồng duyệt đa cấp Nhân viên → Quản lý.
  * Logic chống trùng lịch và ràng buộc ngày lễ hoạt động chuẩn xác.
  * Hủy đơn với đầy đủ kiểm soát điều kiện thời gian.
* Interactive Calendar trực quan: Mỗi ngày hiển thị màu sắc tương ứng trạng thái, click vào ngày tự điền form.
* Điểm danh WFH tích hợp hoàn hảo với module Attendance: Check-in bằng nút bấm, tự động ghi `PRESENT`.
* Toast Notification in-house thay thế hoàn toàn `alert()` trên toàn hệ thống – trải nghiệm người dùng được nâng cao đáng kể.
* Phân quyền RBAC được chuẩn hóa với 5 roles tinh gọn, không còn role dư thừa hay mơ hồ.
* Script migration DynamoDB xử lý dứt điểm bug 500 liên quan đến dữ liệu cũ không tương thích.
