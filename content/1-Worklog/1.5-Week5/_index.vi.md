---
title: "Worklog Tuần 5"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Mục tiêu tuần 5:

* Hoàn thiện hệ thống Thông báo đa kênh (WF4) tích hợp Amazon SNS và EventBridge.
* Xây dựng Analytics Pipeline (WF5) kết hợp DynamoDB, Amazon Athena và Dashboard trực quan.
* Phát triển toàn bộ Module Quản lý Công việc & Sự cố (WF8) với đầy đủ RBAC và tích hợp thông báo tự động.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|-----|-----------|--------------|-----------------|----------------|
| 2 | - Hoàn thiện WF4 – Module Notifications: <br>&emsp; + Định nghĩa 5 Message Templates: `AttendanceRecorded`, `AttendanceRejected`, `UnknownFaceDetected`, `SecurityIncidentCreated`, `Custom`. <br>&emsp; + Cấu hình đa kênh: EMAIL, SMS, PUSH, TEAMS, SLACK, WEBHOOK. <br>&emsp; + Tích hợp `publish_to_topic()` qua Amazon SNS ARN thực. <br>&emsp; + Audit Trail: Mỗi thông báo lưu vào DynamoDB `smart-campus-notifications` với trạng thái `SENT`/`FAILED`. <br>&emsp; + Publish sự kiện `NotificationSent` lên EventBridge sau khi gửi thành công. | 21/07/2026 | 21/07/2026 | https://docs.aws.amazon.com/sns/ |
| 3 | - Xây dựng Analytics Pipeline (WF5): <br>&emsp; + **Phase 1 (DynamoDB)**: Truy vấn trực tiếp bảng `smart-campus-attendance`. <br>&emsp; + **Phase 2 (Athena/S3 Data Lake)**: Lambda Worker lắng nghe `AttendanceRecorded` → stream qua Kinesis Firehose → S3 phân vùng `year/month/day`. <br>&emsp; + Cấu hình AWS Glue Crawler để tự động detect schema và cập nhật Data Catalog. <br>&emsp; + Thiết lập Athena để truy vấn S3 bằng SQL chuẩn. <br>&emsp; + 4 REST Endpoints: summary, daily, trend, user-stats. | 22/07/2026 | 22/07/2026 | https://docs.aws.amazon.com/athena/ |
| 4 | - Xây dựng trang `Analytics.jsx` (Frontend) với Recharts: <br>&emsp; + 4 KPI Cards: Tỉ lệ điểm danh, Tổng user, Số ca ghi nhận, Số người vắng nhiều nhất. <br>&emsp; + Area Chart: Xu hướng điểm danh theo ngày (Có mặt vs Đi muộn). <br>&emsp; + Bar Chart: Top 8 người có tỉ lệ điểm danh thấp nhất. <br>&emsp; + DataSource Badge: Hiển thị nguồn dữ liệu thực tế (Athena / DynamoDB). <br> - Thiết kế và đặc tả nghiệp vụ Module Quản lý Công việc (WF8): 3 loại Task, State Machine, RBAC. | 23/07/2026 | 23/07/2026 | Recharts Docs |
| 5 | - Phát triển Backend Module `tasks` (WF8): <br>&emsp; + DynamoDB Table `smart-campus-tasks`: 13 attributes, 3 GSI. <br>&emsp; + API CRUD: Tạo, Xem, Cập nhật, Xóa task (với RBAC: Admin hard-delete, Reporter soft-delete). <br>&emsp; + Subtask: Khóa department theo Task cha, lọc nhân viên theo phòng ban. <br>&emsp; + S3 Attachment: Upload file đính kèm, Dynamic Presigned URL khi trả về danh sách Task. <br>&emsp; + Validation: Không cho tạo Task với deadline trong quá khứ. | 24/07/2026 | 24/07/2026 | DynamoDB Docs |
| 6 | - Tích hợp **7 điểm thông báo tự động** vào vòng đời Task: Tạo task, Báo cáo sự cố, Phân công lại, Nộp báo cáo, Duyệt hoàn thành, Từ chối, Thay đổi trạng thái. <br> - Fix bug nghiêm trọng: Notification schema dùng camelCase thay vì snake_case → DynamoDB từ chối lưu (silent failure). <br> - Áp dụng kỹ thuật **Hybrid Chunk Pagination** cho danh sách Tasks (DynamoDB NoSQL không hỗ trợ COUNT). <br> - Nâng cấp `Header.jsx`: Dropdown chuông 🔔 hiển thị 5 thông báo mới nhất, polling mỗi 30 giây. | 25/07/2026 | 25/07/2026 | FastAPI Docs |

### Kết quả đạt được tuần 5:

* Hệ thống Thông báo (WF4) hoàn chỉnh:
  * Gửi thông báo thực qua Amazon SNS Email.
  * 5 loại template được định nghĩa sẵn, dễ dàng mở rộng thêm.
  * Audit Trail đầy đủ trong DynamoDB cho tất cả thông báo đã gửi.
* Analytics Pipeline (WF5) với 2 nguồn dữ liệu linh hoạt:
  * DynamoDB: Luôn sẵn sàng, phản hồi nhanh.
  * Athena/S3: Phân tích dữ liệu lịch sử lớn, tự động fallback về DynamoDB nếu Athena lỗi.
  * Dashboard trực quan với Recharts: Area Chart, Bar Chart, KPI Cards.
* Module WF8 (Quản lý Công việc) hoàn chỉnh với đầy đủ:
  * CRUD Task + Subtask + Attachment (S3 Presigned URL).
  * RBAC: Admin, Manager, Reporter có quyền hạn khác nhau.
  * 7 điểm thông báo tự động khi vòng đời task thay đổi.
  * Phân trang NoSQL thông minh: Hybrid Chunk Pagination tránh vấn đề COUNT của DynamoDB.
* Khắc phục bug nghiêm trọng: Notification schema mismatch (silent failure) được phát hiện và vá triệt để.
