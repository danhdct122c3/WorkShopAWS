import os
import re
from datetime import datetime, timedelta

vi_data = {
    1: {
        "days": [
            "- Đọc quy định, tìm hiểu mô hình Cloud Computing (IaaS, PaaS, SaaS).<br>- Phân tích AWS Global Infrastructure (Region, AZ) và các dịch vụ cốt lõi.",
            "- Khởi tạo tài khoản AWS Free Tier và làm quen với AWS Console.<br>- Nghiên cứu IAM (Users, Roles, Policies) và nguyên tắc Least Privilege.",
            "- Thiết lập AWS Budgets và cài đặt, cấu hình AWS CLI.<br>- Tạo IAM User và thực hành gọi API thông qua AWS CLI.",
            "- Tìm hiểu kiến trúc Serverless, Event-Driven Architecture (Pub/Sub, Streaming).<br>- Nghiên cứu cơ chế hoạt động của Amazon EventBridge, API Gateway và AWS Lambda.",
            "- Viết hàm Lambda `Hello World` và cấu hình trigger từ API Gateway.<br>- Kiểm thử thành công REST endpoint Serverless bằng Postman."
        ],
        "result": "- Nắm được nền tảng AWS, cài đặt thành công CLI và tạo REST endpoint Serverless đầu tiên."
    },
    2: {
        "days": [
            "- Cập nhật yêu cầu đồ án Smart Campus, xác định các nhóm user và use-case.<br>- Bắt đầu phân tích bài toán Backend và định hình các dịch vụ AWS cần thiết.",
            "- Thiết kế kiến trúc tổng thể hệ thống theo hướng Event-Driven Serverless.<br>- Định nghĩa 8 luồng nghiệp vụ cốt lõi (Auth, Face, Attendance, Notification, v.v.).",
            "- Khởi tạo dự án theo cấu trúc Monorepo, cài đặt môi trường Python 3.11+.<br>- Xây dựng tài liệu kiến trúc Backend chi tiết và thống nhất stack công nghệ.",
            "- Khởi tạo thủ công 5 bảng cơ sở dữ liệu trên DynamoDB qua AWS Console.<br>- Thiết lập S3 Bucket và Amazon Rekognition Collection cho xử lý hình ảnh.",
            "- Hoàn thiện tài liệu thiết kế database (ERD) và các kịch bản API Backend.<br>- Rà soát, chuẩn bị các library cần thiết (boto3, FastAPI) cho tuần tiếp theo."
        ],
        "result": "- Khởi tạo xong Monorepo Python, cấu hình xong hạ tầng AWS cơ bản (DynamoDB, S3, Rekognition) và chốt kiến trúc."
    },
    3: {
        "days": [
            "- Khởi tạo FastAPI server theo cấu trúc module hóa (app/modules/).<br>- Thiết lập CORS Middleware và hệ thống Error Handler tập trung.",
            "- Tích hợp thư viện boto3 để kết nối Backend tới DynamoDB, S3 và Rekognition.<br>- Viết các hàm utilities/helpers phục vụ cho thao tác AWS services.",
            "- Phát triển module `users` và `faces` theo chuẩn Repository – Service – Router.<br>- Viết API phục vụ quản lý thông tin người dùng cơ bản.",
            "- Phát triển module `attendance` và `notifications`, xử lý nghiệp vụ ghi log điểm danh.<br>- Bổ sung module `reports` và `ai_assistant`, xây dựng mock data để kiểm thử.",
            "- Tổng hợp và cấu hình Swagger UI để tự động sinh tài liệu API (API Docs).<br>- Kiểm thử chéo toàn bộ các endpoint đã phát triển thông qua Swagger UI."
        ],
        "result": "- Xây dựng thành công bộ khung FastAPI, hoàn thiện 7 module cốt lõi chuẩn Repository-Pattern và test API qua Swagger."
    },
    4: {
        "days": [
            "- Thiết lập S3 Bucket (Block Public Access) và viết lớp wrapper `rekognition.py`.<br>- Tích hợp các hàm `IndexFaces` và `SearchFacesByImage` vào Backend.",
            "- Hoàn thành API đăng ký khuôn mặt (nhận ảnh base64, decode, validate).<br>- Xử lý lưu ảnh gốc lên S3 và gọi IndexFaces để sinh `faceId` lưu vào DynamoDB.",
            "- Xây dựng Rule Engine điểm danh với 3 ca làm việc (Morning, Afternoon, Evening).<br>- Cài đặt logic tự động phân loại trạng thái điểm danh (PRESENT, LATE, REJECTED).",
            "- Tối ưu truy vấn bằng cách tạo thêm GSI `date-index`, `userid-index` trên DynamoDB.<br>- Áp dụng cơ chế Idempotency chống điểm danh trùng lặp trong cùng một ca.",
            "- Cấu hình đẩy sự kiện `AttendanceRecorded`, `AttendanceRejected` lên EventBridge.<br>- Xử lý lỗi boto3 không hỗ trợ Float bằng cách parse BoundingBox sang String."
        ],
        "result": "- Hoàn thành luồng đăng ký khuôn mặt và Rule Engine điểm danh thông minh, tích hợp thành công Rekognition & EventBridge."
    },
    5: {
        "days": [
            "- Hoàn thiện module Notifications với 5 Message Template (Attendance, Security, v.v.).<br>- Tích hợp Amazon SNS ARN để đẩy thông báo đa kênh, ghi Audit Trail vào DynamoDB.",
            "- Xây dựng luồng xử lý sự kiện: Lambda Worker lắng nghe EventBridge và gọi SNS.<br>- Triển khai Analytics Pipeline (Phase 1): Viết API truy vấn trực tiếp từ DynamoDB.",
            "- Triển khai Analytics (Phase 2): Dựng Data Lake bằng Lambda stream tới Kinesis Firehose.<br>- Đẩy dữ liệu xuống S3 phân vùng động (year/month) và chạy AWS Glue Crawler.",
            "- Viết câu truy vấn SQL chuẩn qua Amazon Athena để lấy dữ liệu thống kê từ S3.<br>- Xây dựng 4 REST endpoint cho Analytics (summary, daily, trend) với fallback.",
            "- Phát triển module Quản lý công việc (Tasks) với cấu trúc 13 attributes và 3 GSI.<br>- Vá bug schema Notification dùng camelCase bị DynamoDB từ chối ghi ngầm."
        ],
        "result": "- Triển khai thành công Data Lake (Firehose, Glue, Athena) và hệ thống thông báo sự kiện qua SNS."
    },
    6: {
        "days": [
            "- Tích hợp AWS Cognito cho luồng Auth: Gọi `admin_create_user` để tạo tài khoản.<br>- Xử lý logic Cognito tự sinh Temporary Password mà không cần email thủ công.",
            "- Xây dựng API `respond-challenge` để xử lý trạng thái NEW_PASSWORD_REQUIRED.<br>- Thêm middleware kiểm tra JWT token và phân quyền RBAC.",
            "- Hoàn thiện API đăng nhập: Trả về JWT Access Token và Id Token cho client.<br>- Cập nhật API tự đăng ký khuôn mặt mà không cần qua Admin.",
            "- Thêm rào chắn chống trùng lặp khuôn mặt: Gọi `SearchFacesByImage` trước khi `IndexFaces`.<br>- Phát triển tính năng đăng nhập bằng khuôn mặt trả về JWT thay thế mật khẩu.",
            "- Rà soát phân quyền API Backend theo RBAC: Chặn các role không hợp lệ truy cập.<br>- Khắc phục lỗi rò rỉ, tối ưu bảo mật theo 6 trụ cột AWS Well-Architected Framework."
        ],
        "result": "- Tích hợp hoàn chỉnh AWS Cognito, bảo mật toàn bộ API bằng JWT, và hoàn thiện RBAC Backend."
    },
    7: {
        "days": [
            "- Thiết kế bảng DynamoDB `smart-campus-leaves` với các GSI phục vụ truy vấn.<br>- Viết API tạo đơn xin nghỉ phép (Leave Request) hỗ trợ WFH, ANNUAL_LEAVE, v.v.",
            "- Phát triển logic Backend kiểm tra chồng lấn khoảng thời gian (date_from - date_to).<br>- Chặn các đơn trùng lặp với lịch đã PENDING/APPROVED hoặc trùng ngày lễ.",
            "- Viết API xét duyệt đa cấp: Cho phép Manager/Admin duyệt hoặc từ chối đơn nghỉ phép.<br>- Phát triển API Hủy đơn dành riêng cho user, kiểm tra ràng buộc thời gian hợp lệ.",
            "- Tích hợp logic đồng bộ tự động trạng thái điểm danh PRESENT cho ngày WFH.<br>- Bổ sung API cấu hình Quản lý Ngày lễ (Holidays) dành riêng cho role Admin.",
            "- Chuẩn hóa lại các enum role trong Backend (ADMIN, DIRECTOR, MANAGER, STAFF, TECHNICIAN).<br>- Thêm interceptor giới hạn quyền STAFF chỉ được tạo task loại INCIDENT."
        ],
        "result": "- Hoàn thiện module Leave Management với logic kiểm tra chống chồng lấn phức tạp và đồng bộ sự kiện điểm danh."
    },
    8: {
        "days": [
            "- Tích hợp AWS X-Ray SDK (Distributed Tracing) bằng hàm `patch_all()` trong FastAPI.<br>- Theo dõi toàn bộ lời gọi boto3 tới DynamoDB, Rekognition, S3 trên X-Ray Console.",
            "- Xử lý sự cố xung đột Segment X-Ray trên môi trường AWS Lambda bằng middleware.<br>- Thiết lập CloudWatch Alarm theo dõi metric Errors (5xx) của Lambda backend.",
            "- Cấu hình kết nối CloudWatch Alarm với SNS Topic để gửi email cảnh báo khi crash.<br>- Phân tách logic bắt lỗi 4xx khỏi 5xx để tránh False Alarm.",
            "- Triển khai kiến trúc Amazon SQS: Chèn SQS làm Buffer giữa EventBridge và Lambda.<br>- Tạo queue xử lý Analytics, Notification và cấu hình Partial Batch Response.",
            "- Thiết lập Dead Letter Queue (DLQ) hứng message lỗi để retry tự động.<br>- Rà soát source code Backend, đóng gói artifacts và hoàn tất báo cáo kỹ thuật."
        ],
        "result": "- Hệ thống Backend đạt tiêu chuẩn production với X-Ray Tracing, CloudWatch Alarms và kiến trúc SQS Buffer mạnh mẽ."
    }
}

en_data = {
    1: {
        "days": [
            "- Read regulations, understand Cloud Computing models (IaaS, PaaS, SaaS).<br>- Analyze AWS Global Infrastructure (Region, AZ) and core services.",
            "- Create AWS Free Tier account and familiarize with AWS Management Console.<br>- Research IAM (Users, Roles, Policies) and Least Privilege principle.",
            "- Setup AWS Budgets and install, configure AWS CLI.<br>- Create IAM User and practice API calls via AWS CLI.",
            "- Learn Serverless architecture, Event-Driven Architecture (Pub/Sub, Streaming).<br>- Study mechanics of Amazon EventBridge, API Gateway, and AWS Lambda.",
            "- Write `Hello World` Lambda function and configure API Gateway trigger.<br>- Successfully test Serverless REST endpoint using Postman."
        ],
        "result": "- Mastered AWS fundamentals, successfully installed CLI and created the first Serverless REST endpoint."
    },
    2: {
        "days": [
            "- Update Smart Campus requirements, identify user groups and use-cases.<br>- Begin Backend system analysis and determine required AWS services.",
            "- Design overall system architecture following Event-Driven Serverless approach.<br>- Define 8 core business workflows (Auth, Face, Attendance, Notification, etc.).",
            "- Initialize project using Monorepo structure, setup Python 3.11+ environment.<br>- Build detailed Backend architecture document and standardize tech stack.",
            "- Manually provision 5 database tables on DynamoDB via AWS Console.<br>- Setup S3 Bucket and Amazon Rekognition Collection for image processing.",
            "- Finalize database design document (ERD) and Backend API scenarios.<br>- Review and prepare necessary libraries (boto3, FastAPI) for next week."
        ],
        "result": "- Initialized Python Monorepo, configured basic AWS infrastructure (DynamoDB, S3, Rekognition) and finalized architecture."
    },
    3: {
        "days": [
            "- Initialize FastAPI server with modular structure (app/modules/).<br>- Setup CORS Middleware and centralized Error Handler system.",
            "- Integrate boto3 library to connect Backend to DynamoDB, S3, and Rekognition.<br>- Write utilities/helpers functions for AWS service operations.",
            "- Develop `users` and `faces` modules following Repository-Service-Router pattern.<br>- Write APIs for managing basic user information.",
            "- Develop `attendance` and `notifications` modules, processing attendance logs.<br>- Add `reports` and `ai_assistant` modules, build mock data for testing.",
            "- Consolidate and configure Swagger UI to auto-generate API Docs.<br>- Cross-test all developed endpoints via Swagger UI."
        ],
        "result": "- Successfully built FastAPI framework, completed 7 core modules with Repository-Pattern and tested APIs via Swagger."
    },
    4: {
        "days": [
            "- Setup S3 Bucket (Block Public Access) and write `rekognition.py` wrapper.<br>- Integrate `IndexFaces` and `SearchFacesByImage` functions into Backend.",
            "- Complete face registration API (receive base64 image, decode, validate).<br>- Save original image to S3 and call IndexFaces to generate `faceId` for DynamoDB.",
            "- Build Attendance Rule Engine with 3 shifts (Morning, Afternoon, Evening).<br>- Implement logic to auto-classify attendance status (PRESENT, LATE, REJECTED).",
            "- Optimize queries by creating GSI `date-index`, `userid-index` on DynamoDB.<br>- Apply Idempotency mechanism to prevent duplicate attendance in the same shift.",
            "- Configure pushing `AttendanceRecorded`, `AttendanceRejected` events to EventBridge.<br>- Fix boto3 Float unsupported error by parsing BoundingBox to String."
        ],
        "result": "- Completed face registration flow and smart attendance Rule Engine, successfully integrated Rekognition & EventBridge."
    },
    5: {
        "days": [
            "- Complete Notifications module with 5 Message Templates (Attendance, Security, etc.).<br>- Integrate Amazon SNS ARN to push multi-channel alerts, record Audit Trail in DynamoDB.",
            "- Build event processing flow: Lambda Worker listens to EventBridge and calls SNS.<br>- Deploy Analytics Pipeline (Phase 1): Write direct DynamoDB query APIs.",
            "- Deploy Analytics (Phase 2): Build Data Lake with Lambda streaming to Kinesis Firehose.<br>- Push data to dynamically partitioned S3 (year/month) and run AWS Glue Crawler.",
            "- Write standard SQL queries via Amazon Athena to fetch statistical data from S3.<br>- Build 4 REST endpoints for Analytics (summary, daily, trend) with fallback.",
            "- Develop Tasks Management module with 13 attributes and 3 GSIs structure.<br>- Patch camelCase Notification schema bug causing silent write failures in DynamoDB."
        ],
        "result": "- Successfully deployed Data Lake (Firehose, Glue, Athena) and SNS event notification system."
    },
    6: {
        "days": [
            "- Integrate AWS Cognito for Auth flow: Call `admin_create_user` to create accounts.<br>- Handle logic for Cognito auto-generating Temporary Password without manual emails.",
            "- Build `respond-challenge` API to handle NEW_PASSWORD_REQUIRED state.<br>- Add middleware to verify JWT tokens and enforce RBAC authorization.",
            "- Finalize login API: Return JWT Access Token and Id Token to client.<br>- Update self-service face registration API bypassing Admin requirement.",
            "- Add face duplication barrier: Call `SearchFacesByImage` before `IndexFaces`.<br>- Develop face login feature returning JWT instead of using password.",
            "- Review Backend API permissions via RBAC: Block invalid roles from accessing endpoints.<br>- Fix memory leaks, optimize security following AWS Well-Architected Framework 6 pillars."
        ],
        "result": "- Fully integrated AWS Cognito, secured all APIs with JWT, and finalized Backend RBAC."
    },
    7: {
        "days": [
            "- Design DynamoDB `smart-campus-leaves` table with GSIs for status queries.<br>- Write Leave Request API supporting WFH, ANNUAL_LEAVE, etc.",
            "- Develop Backend logic checking overlapping timeframes (date_from - date_to).<br>- Block duplicate requests against PENDING/APPROVED schedules or holidays.",
            "- Write multi-level approval API: Allow Manager/Admin to approve/reject leaves.<br>- Develop Cancel Request API specifically for users, validating time constraints.",
            "- Integrate logic to auto-sync PRESENT attendance status for approved WFH days.<br>- Add Holidays configuration API specifically for Admin role.",
            "- Standardize role enums in Backend (ADMIN, DIRECTOR, MANAGER, STAFF, TECHNICIAN).<br>- Add interceptor limiting STAFF permissions to only create INCIDENT tasks."
        ],
        "result": "- Completed Leave Management module with complex anti-overlap checking logic and attendance event synchronization."
    },
    8: {
        "days": [
            "- Integrate AWS X-Ray SDK (Distributed Tracing) using `patch_all()` in FastAPI.<br>- Monitor all boto3 calls to DynamoDB, Rekognition, S3 on X-Ray Console.",
            "- Resolve X-Ray Segment conflict issues on AWS Lambda environment via middleware.<br>- Setup CloudWatch Alarm monitoring Errors (5xx) metric for Backend Lambda.",
            "- Configure CloudWatch Alarm connection with SNS Topic to send crash email alerts.<br>- Separate 4xx (user error) catch logic from 5xx to prevent False Alarms.",
            "- Deploy Amazon SQS architecture: Insert SQS as Buffer between EventBridge and Lambda.<br>- Create queues processing Analytics, Notifications and configure Partial Batch Response.",
            "- Setup Dead Letter Queue (DLQ) catching error messages for automatic retry.<br>- Review Backend source code, package artifacts, and finalize technical reports."
        ],
        "result": "- Backend system achieved production standards with X-Ray Tracing, CloudWatch Alarms, and robust SQS Buffer architecture."
    }
}

start_date = datetime(2026, 6, 22)

def process_file(lang, week_num, file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    data = vi_data[week_num] if lang == 'vi' else en_data[week_num]
    
    week_start = start_date + timedelta(days=7 * (week_num - 1))
    
    table_lines = [
        "| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |" if lang == 'vi' else "| Day | Tasks | Start Date | End Date | References |",
        "|---|---|---|---|---|"
    ]
    
    for i in range(5):
        day = week_start + timedelta(days=i)
        date_str = day.strftime('%d/%m/%Y')
        day_num = i + 2 if lang == 'vi' else ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'][i]
        task_text = data['days'][i]
        
        doc_link = "https://docs.aws.amazon.com/" if i % 2 == 0 else "https://cloudjourney.awsstudygroup.com/"
        table_lines.append(f"| {day_num} | {task_text} | {date_str} | {date_str} | {doc_link} |")

    table_content = "\n".join(table_lines) + "\n\n"
    
    if lang == 'vi':
        pattern = r"(## 2\. Nhật ký công việc chi tiết\n\n).*?(?=\n\n## 3\.)"
    else:
        pattern = r"(## 2\. Detailed Worklog\n\n).*?(?=\n\n## 3\.)"
        
    content = re.sub(pattern, r"\1" + table_content, content, flags=re.DOTALL)
    
    if lang == 'vi':
        result_pattern = r"(## 3\. Các kết quả đạt được\n\n).*?(?=\n\n## 4\.)"
    else:
        result_pattern = r"(## 3\. Achieved Results\n\n).*?(?=\n\n## 4\.)"
        
    content = re.sub(result_pattern, r"\1" + data['result'] + "\n", content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"d:\AWS\fcj-workshop-template\content\1-Worklog"
for w in range(1, 9):
    vi_path = os.path.join(base_dir, f"{w}-Week{w}", "_index.vi.md")
    en_path = os.path.join(base_dir, f"{w}-Week{w}", "_index.md")
    process_file('vi', w, vi_path)
    process_file('en', w, en_path)
    print(f"Updated week {w}")
