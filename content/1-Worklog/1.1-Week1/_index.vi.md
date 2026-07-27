---
title: "Worklog Tuần 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---



### Mục tiêu tuần 1:

* Làm quen với môi trường, tìm hiểu về nội quy, các lưu ý tại đơn vị thực tập
* Hiểu dịch vụ AWS cơ bản, cách dùng console & CLI.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |     |     |     |
| -----| -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| --------------| -----------------| -------------------------------------------| -----| -----| -----|
| 2   | - Tìm hiểu quy định, lộ trình và yêu cầu của chương trình thực tập tại FCAJ.  <br> - Đọc và lưu ý các nội quy, quy định tại đơn vị thực tập. <br> - Đọc tài liệu hướng dẫn về tiêu chí đánh giá project. <br> - Tìm hiểu các yêu cầu bắt buộc như báo cáo, blog, sơ đồ kiến trúc và số lượng dịch vụ AWS cần sử dụng. <br> - Xác định định hướng xây dựng một ứng dụng thực tế trên nền tảng AWS. <br> - Ghi nhận các yêu cầu liên quan đến project, báo cáo, blog và thời gian tham gia.                                                                                                                                                                                                                                   | 22/06/2026   | 22/06/2026      | https://hcm-rules.awsfcaj.com/            |     |     |     |
| 3   | - Đọc tài liệu hướng dẫn thực hiện project tại FCAJ. <br> - Tìm hiểu các tiêu chí đánh giá project kỹ thuật. <br> - Tìm hiểu yêu cầu về bài toán thực tế, sơ đồ kiến trúc và các dịch vụ AWS.  <br> - Tạo AWS Free Tier account <br> - Tìm hiểu AWS Console & AWS CLI <br> - <br> - Tìm hiểu các khái niệm cơ bản về điện toán đám mây.                                                                                                                                                                                                                                                                                                                                                                                     | 23/06/2026   | 23/06/2026      | <https://cloudjourney.awsstudygroup.com/> |     |     |     |
| 4   | <br> - Tìm hiểu cấu trúc AWS Global Infrastructure. <br> - Tìm hiểu sự khác nhau giữa các dịch vụ global và các dịch vụ hoạt động theo Region. <br> - Làm quen với AWS Management Console. <br>  **Thực hành:** <br>&emsp; + Tạo AWS account <br>&emsp; + Cài AWS CLI & cấu hình <br> &emsp; + Cách sử dụng AWS CLI      <br> &emsp;  + Thử chuyển đổi giữa các Region và tìm kiếm một số dịch vụ AWS.  <br> &emsp; + Quan sát sự khác nhau của tài nguyên giữa các Region.                                                                                                                                                                                                                                                 | 24/06/2026   | 24/06/2026      | <https://cloudjourney.awsstudygroup.com/> |     |     |     |
| 5   | <br> - Tìm hiểu AWS Identity and Access Management. <br> - Tìm hiểu AWS Billing Dashboard, AWS Budgets và Cost Explorer. <br> - Nghiên cứu các khái niệm IAM User, User Group, Role và Policy.  <br>  - Tìm hiểu nguyên tắc Least Privilege. <br>    - Tìm hiểu vai trò của IAM trong việc kiểm soát quyền truy cập vào các tài nguyên AWS.   <br>  - Ghi chú các rủi ro có thể phát sinh chi phí khi sử dụng tài nguyên AWS.   <br> **Thực hành** <br>&emsp; +Truy cập IAM Dashboard trên AWS Management Console. <br>&emsp; + Quan sát cấu trúc IAM User, Role và Policy.<br>&emsp; + Tìm hiểu cấu trúc cơ bản của một IAM Policy.<br>&emsp; + Truy cập Billing Dashboard để tìm hiểu về thông tin chi phí và mức sử dụng | 25/06/2026   | 25/06/2026      | <https://cloudjourney.awsstudygroup.com/> |     |     |     |
| 6   | - Tìm hiểu các nhóm dịch vụ chính của AWS<br>  - Nghiên cứu nhóm dịch vụ compute, storage, database, networking và monitoring.    <br> - Tìm hiểu vai trò cơ bản của EC2, Lambda, S3, RDS, DynamoDB và CloudWatch. <br> - Tìm hiểu về mô hình triển khai truyền thống. <br> - Tìm hiểu về mô hình triển khai serverless. <br> **Thực hành** <br>&emsp; + Làm quen với giao diện ủa các dịch vụ như S3, AWS Lambda, RDS Database và Amazon EC2. <br>&emsp; + Tạo thử dịch vụ Amazon S3, RDs Database và EC2 để tìm hiểu và xóa sau khi thực hành.                                                                                                                                                                            | 25/06/2026   | 25/06/2026      | <https://cloudjourney.awsstudygroup.com/> |     |     |     |


### Kết quả đạt được tuần 1:

* Hiểu AWS là gì và nắm được các nhóm dịch vụ cơ bản: 
  * Compute
  * Storage
  * Networking 
  * Database
  * ...

* Đã tạo và cấu hình AWS Free Tier account thành công.

* Làm quen với AWS Management Console và biết cách tìm, truy cập, sử dụng dịch vụ từ giao diện web.

* Cài đặt và cấu hình AWS CLI trên máy tính bao gồm:
  * Access Key
  * Secret Key
  * Region mặc định
  * ...

* Sử dụng AWS CLI để thực hiện các thao tác cơ bản như:

  * Kiểm tra thông tin tài khoản & cấu hình
  * Lấy danh sách region
  * Xem dịch vụ EC2
  * Tạo và quản lý key pair
  * Kiểm tra thông tin dịch vụ đang chạy
  * ...

* Có khả năng kết nối giữa giao diện web và CLI để quản lý tài nguyên AWS song song.
* ...


