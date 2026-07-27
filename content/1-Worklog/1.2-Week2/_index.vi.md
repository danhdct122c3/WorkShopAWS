---
title: "Worklog Tuần 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---



### Mục tiêu tuần 2:

* Kết nối, làm quen với các thành viên trong First Cloud AI Journey.
* Hiểu dịch vụ AWS cơ bản, cách dùng console & CLI.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu                            |     |
| -----| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| --------------| -----------------| -------------------------------------------| -----|
| 2   | - Xem lại các yêu cầu và tiêu chí đánh giá đối với project kỹ thuật tại FCAJ. <br> - Tìm hiểu một số ý tưởng project có thể triển khai trên nền tảng AWS. <br> - Nghiên cứu các bài toán thực tế phù hợp với mô hình Cloud và Serverless. <br> - Đánh giá sơ bộ các ý tưởng dựa trên tính thực tế, phạm vi chức năng, khả năng mở rộng và khả năng tích hợp các dịch vụ AWS. <br> - Xác định hướng xây dựng một hệ thống hỗ trợ hoạt động quản lý trong môi trường trường học hoặc tổ chức. <br> - **Thực hành:** <br>&emsp; + Lập danh sách các ý tưởng project tiềm năng. <br>&emsp; + So sánh ưu điểm, nhược điểm và khả năng triển khai của từng ý tưởng. <br>&emsp; + Ghi chú phạm vi, các dịch vụ, chức năng dự kiến có thể triển khai cho từng phương án.                                                                                                                                           | 29/06/2026   | 29/06/2026      | <https://cloudjourney.awsstudygroup.com/> |     |
| 3   | - Lựa chọn đề tài ban đầu Smart Campus: Hệ thống quản lý chấm công. <br> - Tìm hiểu bài toán quản lý chấm công trong trường học hoặc tổ chức. <br> - Xác định các đối tượng sử dụng chính của hệ thống. <br> - Xác định các chức năng cơ bản như quản lý người dùng, check-in, check-out và xem lịch sử chấm công. <br> - Phân tích sơ bộ quy trình chấm công từ khi người dùng thực hiện check-in đến khi dữ liệu được lưu trữ. <br> **Thực hành:** <br>&emsp; + Xác định nghiệp vụ ban đầu của hệ thống.<br>&emsp; + Liệt kê các chức năng chính theo từng vai trò.   <br>&emsp;  + Phác thảo luồng nghiệp vụ check-in và check-out.<br>                                                                                                                                                                                                                                                                 | 12/08/2025   | 12/08/2025      | <https://cloudjourney.awsstudygroup.com/> |     |
| 4   | - Phân tích chi tiết nghiệp vụ của hệ thống quản lý chấm công. <br>- Xác định các vai trò và quyền hạn cơ bản trong hệ thống. <br>                                                                                                                                                    - Xây dựng luồng hoạt động cho chức năng check-in và check-out. <br>- Xác định các thông tin cần lưu trữ như thông tin người dùng, thời gian check-in, thời gian check-out và lịch sử chấm công. <br>- Tìm hiểu các trường hợp như đi trễ, quên check-out hoặc dữ liệu chấm công không hợp lệ. <br>**Thực hành:** <br>&emsp; + Vẽ sơ đồ luồng nghiệp vụ chấm công bằng Draw.io. <br>&emsp; + Phác thảo cấu trúc dữ liệu ban đầu cho User. <br>&emsp; <br>&emsp; + Xác định các vai trò và quyền hạn cơ bản trong hệ thống.<br>&emsp; | 14/08/2025   | 15/08/2025      | <https://cloudjourney.awsstudygroup.com/> |     |
| 5   | - Tìm hiểu các dịch vụ AWS có thể sử dụng cho hệ thống Smart Campus.          <br>- Nghiên cứu AWS Lambda để xử lý nghiệp vụ backend theo mô hình Serverless. <br>- Tìm hiểu Amazon API Gateway để tiếp nhận và định tuyến API request. <br>- Tìm hiểu Amazon DynamoDB và so sánh sơ bộ với Amazon RDS. <br> - Tìm hiểu Amazon CloudWatch để lưu log và giám sát hệ thống. <br>- Tìm hiểu vai trò của IAM Role trong việc cấp quyền giữa các dịch vụ AWS. <br> **Thực hành:** <br>&emsp;  + Làm quen với giao diện Lambda <br>&emsp;  + Làm quen với giao diện DynamoDB <br>&emsp; + Quan sát cách tạo Function và Table.                                                                                                                 | 15/08/2025   | 15/08/2025      | <https://cloudjourney.awsstudygroup.com/> |     |
| 6   | - Tổng hợp yêu cầu nghiệp vụ và các dịch vụ AWS đã nghiên cứu.  <br>  - Lựa chọn các dịch vụ AWS dự kiến sử dụng. <br> - Xác định luồng tổng quát của hệ thống. <br>  **Thực hành:**  <br>&emsp; + Sử dụng Draw.io để xây dựng sơ đồ kiến trúc phiên bản đầu tiên.<br>&emsp;   + Sử dụng AWS Architecture Icons để biểu diễn các dịch vụ AWS.<br>&emsp;   + Mô tả luồng request và luồng xử lý dữ liệu chấm công trong hệ thống.<br>&emsp;                                                                            | 15/08/2025   | 15/08/2025      | <https://cloudjourney.awsstudygroup.com/> |     |


### Kết quả đạt được tuần 2:

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


