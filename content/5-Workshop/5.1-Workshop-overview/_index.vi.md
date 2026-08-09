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

### 2. Sơ đồ kiến trúc
Kiến trúc của hệ thống Smart Campus bao gồm các khối: Frontend & Edge, Authentication, Core API & AI, Asynchronous Event-Driven, Data Analytics, CI/CD Pipeline và Observability.

> **Hình 1 - Sơ đồ Kiến trúc và luồng xử lý Smart Campus**
> ![Architecture Overview](/aws-image/Architechture.png)

**Luồng xử lý tổng thể của hệ thống:**
`Frontend -> CloudFront -> API Gateway -> Lambda -> Rekognition -> DynamoDB -> EventBridge -> SQS -> Lambda Worker -> SNS/SES`
Đồng thời: `EventBridge -> Kinesis Firehose -> S3 Data Lake -> Athena`

### 3. Quy trình xử lý chính (Main Flow) và Kiến trúc bất đồng bộ
Một trong những điểm mấu chốt và quan trọng nhất của kiến trúc này là **hệ thống áp dụng xử lý bất đồng bộ (Asynchronous) cho các tác vụ không cần phản hồi ngay lập tức**.

**Tại sao xử lý bất đồng bộ được chọn?**
Việc điểm danh vào đầu giờ sáng hoặc lúc tan làm sẽ tạo ra một lượng truy cập khổng lồ cùng một lúc (Spike Traffic). Nếu xử lý đồng bộ toàn bộ (lưu DB, nén log, gửi email cảnh báo đi trễ...), hệ thống sẽ phản hồi rất chậm hoặc gây nghẽn cổ chai (bottleneck). Việc tách rời luồng báo cáo và gửi thông báo ra khỏi luồng điểm danh chính (thông qua EventBridge và SQS) giúp API phản hồi cho người dùng trong vòng vài mili-giây, trong khi các tác vụ nặng được đẩy vào hàng đợi (buffer queue) để xử lý dần một cách bền bỉ.

**Luồng xử lý đầu-cuối (End-to-End Main Flow) diễn ra chi tiết qua 16 bước (như đánh số trên sơ đồ):**

*   **(1) User truy cập qua WAF:** Người dùng mở ứng dụng web frontend. Yêu cầu đi qua tường lửa AWS WAF (chặn IP xấu, DDoS) và CDN CloudFront để tải nội dung tĩnh từ S3.
*   **(2) Đăng nhập / Cognito:** Người dùng đăng nhập hệ thống và nhận về mã thông báo xác thực JWT Token từ Amazon Cognito.
*   **(3) API Gateway nhận request:** Giao diện gọi API điểm danh, gửi kèm JWT Token. API Gateway sẽ tự động xác thực token này.
*   **(4) Gọi Lambda Core:** Sau khi xác thực thành công, request được proxy tới AWS Lambda (Core Logic) để bắt đầu xử lý nghiệp vụ.
*   **(5) So khớp khuôn mặt:** Lambda gọi API của Amazon Rekognition để so khớp hình ảnh khuôn mặt được gửi lên với kho dữ liệu khuôn mặt gốc.
*   **(6) Lưu ảnh gốc:** Nhằm mục đích đối soát và audit, ảnh chụp lúc điểm danh được Lambda lưu vào bucket S3 Raw Images.
*   **(7) Lưu trạng thái điểm danh:** Nếu khuôn mặt khớp, Lambda lưu bản ghi điểm danh (Check-in/out) vào Amazon DynamoDB.
*   **(8) Bắn sự kiện (Attendance Event):** Ngay khi lưu xong DB, Lambda bắn (emit) sự kiện điểm danh thành công/thất bại lên Event Bus của Amazon EventBridge. API trả kết quả về cho Frontend ngay lập tức.
*   **(9) Đưa vào hàng đợi:** EventBridge định tuyến sự kiện vào hàng đợi Amazon SQS để làm vùng đệm (buffer) chống nghẽn cổ chai.
*   **(10) Lambda Worker xử lý:** Một hàm Lambda chạy nền lấy các sự kiện từ SQS Queue ra để xử lý các tác vụ tốn thời gian.
*   **(11) Gửi cảnh báo:** Lambda Worker gọi Amazon SNS và Amazon SES để gửi tin nhắn/email (ví dụ: thông báo nhân sự đi trễ hoặc cảnh báo giả mạo).
*   **(12) Đẩy log (Streaming):** Đồng thời tại bước 8, EventBridge cũng định tuyến sự kiện log này sang Amazon Kinesis Data Firehose để phục vụ phân tích.
*   **(13) Gom lô & Ghi dữ liệu:** Firehose tự động gom lô (batch) và nén dữ liệu log, ghi thành file vào S3 Data Lake Bucket.
*   **(14) Truy vấn & Báo cáo:** Giám đốc nhân sự sử dụng Amazon Athena (bằng lệnh SQL) hoặc BI Tools để tạo báo cáo thống kê trực tiếp từ Data Lake mà không cần chạm vào DynamoDB.
*   **(15) Monitoring & Alarm:** Toàn bộ tiến trình hoạt động (Logs & Metrics) được ghi nhận vào Amazon CloudWatch. Nếu phát hiện lỗi (ví dụ Lambda crash), CloudWatch Alarms sẽ cảnh báo ngay cho Ops Team qua Email/Chat.
*   **(16) CI/CD Deploy tự động:** Các thay đổi code của Developer sẽ đi qua AWS CodePipeline và AWS CodeBuild để build và tự động triển khai (Deploy Serverless) lên hạ tầng AWS mà không cần thao tác tay.

### 4. Các dịch vụ trong phạm vi MVP (In-Scope Services)
Để hoàn thành bài lab này, các dịch vụ AWS chính được sử dụng bao gồm:
- **Edge & Frontend:** Amazon S3 (Static Website), Amazon CloudFront, AWS WAF.
- **Authentication & API:** Amazon Cognito, Amazon API Gateway.
- **Core Compute & AI:** AWS Lambda, Amazon Rekognition.
- **Database & Storage:** Amazon DynamoDB, Amazon S3.
- **Event & Queue:** Amazon EventBridge, Amazon SQS, Amazon SNS/SES.
- **Data Analytics:** Amazon Kinesis Data Firehose, Amazon Athena, AWS Glue.
- **CI/CD & Observability:** AWS CodeBuild, AWS CodePipeline, Amazon CloudWatch.
- **Security:** AWS IAM.

### 5. Kết quả mong đợi sau khi kết thúc Workshop
Kết thúc chuỗi bài thực hành này, bạn sẽ dựng hoàn chỉnh một nền tảng doanh nghiệp:
- **Frontend hoạt động tốt:** Có giao diện điểm danh và dashboard quản lý.
- **Xác thực bảo mật đa lớp:** Chống mạo danh bằng IAM Least Privilege, WAF và Cognito JWT.
- **Kiến trúc chịu tải cao:** Ứng dụng thành thạo Event-Driven (EventBridge + SQS) để triệt tiêu tình trạng thắt cổ chai giờ cao điểm.
- **Data Pipeline tự động:** Sở hữu hệ thống Data Lake (Firehose + Athena) tách biệt hoàn toàn OLTP và OLAP.
- **DevOps CI/CD:** Hệ thống CodePipeline tự động build và deploy code mà không cần thao tác tay.
- **Dọn dẹp (Cleanup):** Có khả năng dọn dẹp tài nguyên nhanh chóng để kiểm soát hoàn toàn chi phí AWS.
