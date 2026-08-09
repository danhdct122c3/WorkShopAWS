---
title : "Cấu hình AWS Glue"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.7.2. </b> "
---

#### Khởi tạo Data Catalog với AWS Glue
AWS Glue là dịch vụ Data Integration serverless. Chúng ta sẽ sử dụng tính năng **Glue Crawler** của nó để tự động đọc các file log điểm danh trong S3 bucket và suy luận ra cấu trúc bảng (Table Schema) lưu vào Data Catalog.

**Bước 1: Truy cập AWS Glue**

1. Từ thanh tìm kiếm của AWS Console, gõ **Glue** và chọn dịch vụ **AWS Glue**.
> ![Tìm kiếm Glue](/aws-image/setupGlue/glue1.png)

**Bước 2: Tạo IAM Role cho Glue Crawler**

1. Truy cập vào giao diện IAM, chọn **Roles** và bấm **Create role**.
> ![Vào IAM Roles](/aws-image/setupGlue/glue2.png)
2. Chọn Trusted entity type là **AWS service** và Use case là **Glue**.
> ![Chọn Trusted entity](/aws-image/setupGlue/glue3.png)
3. Tìm kiếm và đính kèm (attach) policy `AWSGlueServiceRole`.
> ![Đính kèm Policy](/aws-image/setupGlue/glue4.png)
4. (Tuỳ chọn) Bạn cần cấp thêm quyền đọc S3 Bucket chứa log cho Role này (ví dụ `AmazonS3FullAccess` hoặc policy tự định nghĩa).
> ![Cấp quyền S3](/aws-image/setupGlue/glue5.png)
5. Đặt tên Role (Ví dụ: `AWSGlueServiceRole-SmartCampus`) và bấm **Create role**.
> ![Tạo Role](/aws-image/setupGlue/glue6.png)

**Bước 3: Tạo Crawler**

1. Quay lại trang AWS Glue, ở menu bên trái chọn **Crawlers** dưới mục **Data Catalog**.
> ![Chọn Crawlers](/aws-image/setupGlue/glue7_1.png)
2. Bấm **Create crawler**.
> ![Bấm Create crawler](/aws-image/setupGlue/glue7_2.png)
3. **Name**: Đặt tên cho crawler (Ví dụ: `smart-campus-crawler`) và bấm **Next**.
> ![Đặt tên Crawler](/aws-image/setupGlue/glue8_1.png)
4. Ở phần **Choose data sources and classifiers**, bấm **Add a data source**.
> ![Add data source](/aws-image/setupGlue/glue8_2.png)
5. Chọn **Data source** là **S3** và trỏ đường dẫn (S3 path) đến bucket chứa file log Data Lake của bạn.
> ![Chọn S3 path](/aws-image/setupGlue/glue9.png)
6. Bấm **Add an S3 data source**.
> ![Bấm Add S3](/aws-image/setupGlue/glue10.png)
7. Đảm bảo Data source đã được thêm vào danh sách và bấm **Next**.
> ![Kiểm tra data source](/aws-image/setupGlue/glue11.png)
8. **Configure security settings**: Chọn IAM Role bạn vừa tạo ở Bước 2.
> ![Chọn IAM Role](/aws-image/setupGlue/glue12.png)
9. Bấm **Next**.
> ![Bấm Next security](/aws-image/setupGlue/glue13.png)
10. **Set output and scheduling**: Ở phần **Target database**, bấm **Add database** để tạo một Database ảo mới.
> ![Bấm Add database](/aws-image/setupGlue/glue14.png)
11. Đặt tên Database (Ví dụ: `smart_campus_db`) và bấm **Create database**.
> ![Tạo database](/aws-image/setupGlue/glue15.png)
12. Quay lại tab tạo Crawler, bấm refresh để cập nhật danh sách Database, sau đó chọn `smart_campus_db` vừa tạo.
> ![Chọn Database](/aws-image/setupGlue/glue16.png)
13. **Crawler schedule**: Chọn **On demand** (chạy thủ công) và bấm **Next**.
> ![Chọn On demand](/aws-image/setupGlue/glue17.png)
14. Xem lại toàn bộ cấu hình và bấm **Create crawler**.
> ![Create crawler](/aws-image/setupGlue/glue18.png)

**Bước 4: Chạy Crawler**

1. Crawler được tạo xong sẽ có thông báo màu xanh. Bấm **Run crawler**.
> ![Run crawler](/aws-image/setupGlue/glue19.png)
2. Chờ khoảng 1-2 phút cho trạng thái crawler chuyển sang **Completed**. Vào mục **Databases** > **Tables**, bạn sẽ thấy bảng dữ liệu mới đã được tạo ra từ S3.
> ![Crawler completed](/aws-image/setupGlue/glue20.png)
