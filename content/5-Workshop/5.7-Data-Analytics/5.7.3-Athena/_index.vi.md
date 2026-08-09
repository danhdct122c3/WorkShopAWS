---
title : "Truy vấn với Amazon Athena"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.7.3. </b> "
---

#### Phân tích dữ liệu với Amazon Athena
Amazon Athena là dịch vụ truy vấn tương tác serverless, giúp bạn dễ dàng phân tích dữ liệu trực tiếp trong S3 bằng SQL tiêu chuẩn. Vì cấu trúc bảng đã được Glue định nghĩa, Athena có thể đọc nó ngay lập tức.

**Bước 1: Truy cập Amazon Athena**

1. Từ thanh tìm kiếm của AWS Console, gõ **Athena** và chọn dịch vụ.
> ![Tìm kiếm Athena](/aws-image/setupAthena/athena1.png)

**Bước 2: Cấu hình Output Location (Bắt buộc trong lần đầu)**

Athena lưu kết quả của mỗi câu truy vấn thành một file trong S3. Nếu bạn truy cập Athena lần đầu trên tài khoản, bạn phải cấu hình vị trí lưu này.
1. Ở bảng điều khiển bên trái, chọn **Query editor**.
> ![Chọn Query editor](/aws-image/setupAthena/athena2.png)
2. Bấm vào tab **Settings** hoặc dòng thông báo yêu cầu cấu hình Query result location.
> ![Tab Settings](/aws-image/setupAthena/athena3.png)
3. Bấm **Manage**. Ở mục **Query result location**, nhập đường dẫn đến một S3 bucket của bạn (Ví dụ: `s3://smart-campus-athena-query-results/`). Bấm **Save**.
> ![Cấu hình Query Result Location](/aws-image/setupAthena/athena4.png)

**Bước 3: Viết câu truy vấn SQL**

1. Quay lại tab **Editor**.
> ![Tab Editor](/aws-image/setupAthena/athena5.png)
2. Ở menu thả xuống **Database** bên trái, chọn `smart_campus_db` (Database bạn đã tạo bằng Glue Crawler).
> ![Chọn Database](/aws-image/setupAthena/athena6.png)
3. Ở ô soạn thảo Query lớn, hãy thử chạy câu lệnh SQL đơn giản nhất để xem tất cả log điểm danh đã được đẩy lên S3:
```sql
SELECT * FROM "smart_campus_db"."<Tên_bảng_S3_của_bạn>" limit 10;
```
> *(Lưu ý: Tên bảng mặc định sẽ là tên thư mục S3 đã được format, bạn có thể click đúp chuột vào tên bảng ở cột bên trái để Athena tự động điền vào khung truy vấn).*
> ![Viết Query](/aws-image/setupAthena/athena7.png)
4. Bấm **Run**.
5. Kéo xuống phần **Query results**, bạn sẽ nhìn thấy dữ liệu định dạng bảng cực kỳ trực quan với các cột như `attendance_id`, `user_id`, `camera_id`, `status` và `timestamp`.
> ![Kết quả Truy vấn](/aws-image/setupAthena/athena8.png)

**Ứng dụng nâng cao:**
Bạn hoàn toàn có thể kết nối Athena với **Amazon QuickSight** (Dịch vụ BI) để vẽ ra các biểu đồ Dashboard trực quan về tình hình đi học của sinh viên, cung cấp cái nhìn tổng quan (insights) cho Ban Giám Hiệu mà không hề làm ảnh hưởng (giảm hiệu năng) của hệ thống điểm danh đang chạy trực tiếp (OLTP).

Đến đây, bạn đã làm chủ hoàn toàn luồng **Dữ liệu lớn (Data Pipeline)** trong Smart Campus!
