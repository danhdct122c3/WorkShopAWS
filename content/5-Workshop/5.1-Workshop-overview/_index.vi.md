---
title : "Giới thiệu"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

### 1. Giới thiệu giải pháp (Use case)
Trong bối cảnh chuyển đổi số giáo dục và doanh nghiệp, việc điểm danh thủ công (quẹt thẻ từ, vân tay) vẫn tồn tại nhiều hạn chế lớn (pain points): ùn tắc vào giờ cao điểm, tình trạng quên thẻ, hoặc gian lận check-in hộ. Các hệ thống máy chủ vật lý nội bộ thường lãng phí tài nguyên khi không có ai sử dụng vào ban đêm, nhưng lại quá tải vào khung giờ 8h00 sáng.

**Smart Campus Platform** ra đời nhằm giải quyết triệt để vấn đề này bằng cách kết hợp trí tuệ nhân tạo nhận diện khuôn mặt (**Amazon Rekognition**) và kiến trúc **100% AWS Serverless**. Hệ thống không chỉ xử lý điểm danh siêu tốc mà còn đảm bảo bảo mật tuyệt đối, tự động hóa luồng thông báo và cung cấp giải pháp phân tích dữ liệu lớn (Big Data) với mức chi phí tối ưu nhất (Pay-as-you-go).

---

### 2. Sơ đồ kiến trúc & Quy trình hoạt động

> **Hình 1 - Sơ đồ Kiến trúc và luồng xử lý Smart Campus**
> ![Architecture Overview](/aws-image/AwsArchitecture.drawio.png)

*(Tài liệu dùng để ghi chú báo cáo/thuyết trình)*

Hệ thống Smart Campus được thiết kế theo kiến trúc Serverless 100% trên nền tảng AWS, áp dụng mô hình Event-Driven Architecture (Kiến trúc hướng sự kiện) nhằm đảm bảo hiệu năng cao, khả năng mở rộng tự động và tối ưu chi phí. Sơ đồ kiến trúc được chia thành các nhóm luồng nghiệp vụ chính như sau:

#### 🛠️ Nhóm 0: CI/CD Pipeline (Triển khai Tự động)
Hệ thống sử dụng bộ công cụ AWS Developer Tools để tự động hóa quá trình kiểm thử và triển khai mã nguồn mỗi khi có thay đổi.
- **C1. Push code:** Developer đẩy mã nguồn mới (Frontend/Backend) lên kho lưu trữ GitHub.
- **C2. Trigger pipeline:** AWS CodePipeline lắng nghe sự kiện từ GitHub và tự động kích hoạt luồng CI/CD.
- **C3. Build & Package:** AWS CodeBuild tải mã nguồn về, biên dịch (Build React) hoặc đóng gói thư viện (Zip Python/FastAPI) tạo thành các bản build hoàn chỉnh.
- **C4. Deploy:** 
  - *Frontend:* CodeBuild đẩy các file tĩnh (HTML/CSS/JS) lên S3 Frontend Bucket.
  - *Backend:* CodeBuild đẩy file zip lên AWS Lambda (`smart-campus-api`) và cập nhật phiên bản mới.

#### 🌐 Nhóm 1: Truy cập & Lấy Token (Access & Auth)
Bảo vệ hệ thống từ vòng ngoài và cung cấp cơ chế xác thực an toàn.
- **1a. Truy cập Web:** Người dùng gửi request truy cập từ trình duyệt.
- **1b. Secure Access (WAF):** AWS WAF kiểm tra IP và các quy tắc bảo mật trước khi cho phép request đi qua.
- **2. Tải giao diện (Serve SPA):** CloudFront lấy nội dung web tĩnh từ S3 Frontend và phân phối nhanh chóng tới người dùng qua mạng CDN toàn cầu.
- **3. Kích hoạt API:** Request nghiệp vụ từ Frontend được đẩy vào API Gateway.
- **4a & 4b. Authenticate:** API Gateway chuyển request đăng nhập cho Lambda. Lambda gọi **Amazon Cognito** để xác thực người dùng và lấy JWT Token trả về cho Frontend.
- **4c. Validate Token:** Các request sau này đều bị API Gateway chặn lại để nhờ Cognito kiểm tra tính hợp lệ của Token trước khi cho đi tiếp.

#### 👤 Nhóm 2: Quản lý Nhân sự & Đăng ký Khuôn mặt
Xử lý dữ liệu người dùng và tạo đặc trưng sinh trắc học.
- **5. Quản lý User:** Lambda đọc/ghi thông tin nhân sự cơ bản vào bảng `Users` trên DynamoDB.
- **6. Yêu cầu Đăng ký:** Luồng đăng ký khuôn mặt nhân viên mới.
- **7. Lưu ảnh gốc:** Lambda tải ảnh gốc (Raw image) lên S3 Images Bucket để làm tài liệu đối chiếu.
- **8. Trích xuất đặc trưng:** Lambda gọi **Amazon Rekognition** (IndexFaces) để trích xuất ma trận sinh trắc học.
- **9. Lưu Metadata:** ID khuôn mặt (FaceID) được lưu vào bảng `Faces` trên DynamoDB.

#### ✅ Nhóm 3: Cốt lõi Điểm danh (Face Attendance)
Đây là luồng xương sống của hệ thống, xử lý độ trễ thấp (< 1s).
- **10. Yêu cầu Điểm danh:** Camera/Kiosk gửi ảnh chụp tại thời gian thực lên API Gateway.
- **11. Lấy thông tin:** Lambda truy vấn bảng `Users` để đối chiếu luật (Ca làm việc, giờ cho phép...).
- **12. Nhận diện:** Lambda gọi Amazon Rekognition (SearchFacesByImage) để so khớp khuôn mặt với độ chính xác cao.
- **13. Ghi nhận:** Bản ghi điểm danh được lưu ngay lập tức vào bảng `Attendance` trên DynamoDB.
- **14. Gửi Email cá nhân:** Lambda dùng **Amazon SES** gửi một biên lai điểm danh (HTML) trực tiếp vào email người đó.
- **15. Publish Event:** Để không làm chậm API, Lambda lập tức bắn sự kiện *"AttendanceRecorded"* (Điểm danh hoàn tất) lên **Amazon EventBridge** và trả về HTTP 200 cho Camera.

#### 🔔 Nhóm 4: Bất đồng bộ (Event-Driven Async Flows)
Xử lý các tác vụ nặng ở background bằng kiến trúc Fan-out (1 sự kiện rẽ nhiều nhánh).
- **16a & 17a. Luồng Thông báo (Notification):** EventBridge đẩy sự kiện vào hàng đợi SQS, kích hoạt `Notification Worker Lambda`. 
- **18. Broadcast via SNS:** Worker này gọi Amazon SNS để "phát sóng" tin nhắn ra các kênh đa phương tiện (SMS, Mobile Push, Chatbot).
- **16b & 17b. Luồng Dữ liệu (Analytics):** Đồng thời, EventBridge cũng đẩy sự kiện vào SQS Analytics, kích hoạt `Analytics Worker Lambda`.
- **19. Lưu Data Lake:** Worker này đóng gói dữ liệu điểm danh thành các file JSON và đẩy vào S3 Data Lake để lưu trữ dài hạn (Cold storage) chi phí thấp.

#### 📊 Nhóm 5: Báo cáo Thống kê (Data Analytics Phase 2)
Xử lý Big Data mà không làm quá tải DynamoDB.
- **20. Catalog Data:** Dịch vụ **AWS Glue** định kỳ quét S3 Data Lake để tự động học hỏi và tạo Lược đồ dữ liệu (Schema).
- **21. Yêu cầu Báo cáo:** User truy cập màn hình Dashboard, API gọi xuống Lambda.
- **22a. Lệnh Truy vấn:** Lambda yêu cầu **Amazon Athena** tính toán số liệu.
- **22b & 22c. Đọc Dữ liệu thô:** Athena dùng lược đồ từ Glue để chạy các câu lệnh SQL siêu tốc quét qua hàng triệu file JSON trên S3 Data Lake và trả kết quả về hiển thị lên Dashboard.

#### 💼 Nhóm 6: Quản lý Công việc & Đơn từ
- **23. Yêu cầu Công việc:** Request giao việc hoặc xin nghỉ được đẩy vào Lambda.
- **24a & 24b. Đọc/Ghi DB:** Dữ liệu lưu vào bảng `Tasks` và `Leaves` độc lập.
- **24c. Lưu Thông báo:** Ghi lịch sử gửi thông báo vào bảng `Notifications`.
- **24d & 24e. Presigned URL Upload:** Thay vì tải file nặng xuyên qua Lambda, Lambda chỉ tạo ra 1 đường dẫn an toàn ngắn hạn (Presigned URL) và trả về. Trình duyệt của User sẽ dùng link này để upload PDF/Hình ảnh trực tiếp lên S3 Images, giúp tối ưu băng thông máy chủ.
- **25. Send Notification:** Gửi email báo có việc mới/đơn mới qua Amazon SES.

#### ⏰ Nhóm 7: Cronjob (Quét trễ hạn)
- **26. Cron Trigger:** **EventBridge Scheduler** được hẹn giờ chạy mỗi X phút, tự động kích hoạt Lambda.
- **27. Quét trễ hạn:** Lambda quét bảng `Tasks` để tìm các công việc sát giờ hoặc đã quá hạn (Overdue).
- **28. Warning Email:** Gửi thư hối thúc nhân viên qua Amazon SES.

#### 🛡️ Nhóm 8: Quản trị, Bảo mật & Giám sát (Cross-cutting)
- **IAM (Identity and Access Management):** Toàn bộ các dịch vụ giao tiếp với nhau bằng nguyên tắc đặc quyền tối thiểu (Least Privilege). Lambda chỉ được ghi S3 bucket cụ thể, không được xóa bucket.
- **X-Ray & CloudWatch:** 
  - Lambda liên tục đẩy Logs/Metrics (số lượng request, thời gian xử lý) về CloudWatch.
  - AWS X-Ray vẽ bản đồ mạng nhện (Trace Map) để theo dõi request đi qua từng dịch vụ mất bao nhiêu mili-giây.
- **CloudWatch Alarms:** Khi phát hiện tỷ lệ lỗi (Faults) vượt mức cho phép, Alarm bị kích hoạt và gọi Amazon SNS bắn cảnh báo khẩn tới điện thoại của đội ngũ kỹ sư.

---

### 3. Các dịch vụ trong phạm vi MVP (In-Scope Services)
Để hoàn thành bài lab này, các dịch vụ AWS chính được sử dụng bao gồm:
- **Edge & Frontend:** Amazon S3 (Static Website), Amazon CloudFront, AWS WAF.
- **Authentication & API:** Amazon Cognito, Amazon API Gateway.
- **Core Compute & AI:** AWS Lambda, Amazon Rekognition.
- **Database & Storage:** Amazon DynamoDB, Amazon S3.
- **Event & Queue:** Amazon EventBridge, Amazon SQS, Amazon SNS/SES.
- **Data Analytics:** Amazon Kinesis Data Firehose, Amazon Athena, AWS Glue.
- **CI/CD & Observability:** AWS CodeBuild, AWS CodePipeline, Amazon CloudWatch.
- **Security:** AWS IAM.

### 4. Kết quả mong đợi sau khi kết thúc Workshop
Kết thúc chuỗi bài thực hành này, bạn sẽ dựng hoàn chỉnh một nền tảng doanh nghiệp:
- **Frontend hoạt động tốt:** Có giao diện điểm danh và dashboard quản lý.
- **Xác thực bảo mật đa lớp:** Chống mạo danh bằng IAM Least Privilege, WAF và Cognito JWT.
- **Kiến trúc chịu tải cao:** Ứng dụng thành thạo Event-Driven (EventBridge + SQS) để triệt tiêu tình trạng thắt cổ chai giờ cao điểm.
- **Data Pipeline tự động:** Sở hữu hệ thống Data Lake (Firehose + Athena) tách biệt hoàn toàn OLTP và OLAP.
- **DevOps CI/CD:** Hệ thống CodePipeline tự động build và deploy code mà không cần thao tác tay.
- **Dọn dẹp (Cleanup):** Có khả năng dọn dẹp tài nguyên nhanh chóng để kiểm soát hoàn toàn chi phí AWS.
