import os
import re

vi_results = {
    1: "- Nắm được nền tảng AWS, cài đặt thành công CLI và tạo REST endpoint Serverless đầu tiên.",
    2: "- Khởi tạo xong Monorepo Python, cấu hình xong hạ tầng AWS cơ bản (DynamoDB, S3, Rekognition) và chốt kiến trúc.",
    3: "- Xây dựng thành công bộ khung FastAPI, hoàn thiện 7 module cốt lõi chuẩn Repository-Pattern và test API qua Swagger.",
    4: "- Hoàn thành luồng đăng ký khuôn mặt và Rule Engine điểm danh thông minh, tích hợp thành công Rekognition & EventBridge.",
    5: "- Triển khai thành công Data Lake (Firehose, Glue, Athena) và hệ thống thông báo sự kiện qua SNS.",
    6: "- Tích hợp hoàn chỉnh AWS Cognito, bảo mật toàn bộ API bằng JWT, và hoàn thiện RBAC Backend.",
    7: "- Hoàn thiện module Leave Management với logic kiểm tra chống chồng lấn phức tạp và đồng bộ sự kiện điểm danh.",
    8: "- Hệ thống Backend đạt tiêu chuẩn production với X-Ray Tracing, CloudWatch Alarms và kiến trúc SQS Buffer mạnh mẽ."
}

en_results = {
    1: "- Mastered AWS fundamentals, successfully installed CLI and created the first Serverless REST endpoint.",
    2: "- Initialized Python Monorepo, configured basic AWS infrastructure (DynamoDB, S3, Rekognition) and finalized architecture.",
    3: "- Successfully built FastAPI framework, completed 7 core modules with Repository-Pattern and tested APIs via Swagger.",
    4: "- Completed face registration flow and smart attendance Rule Engine, successfully integrated Rekognition & EventBridge.",
    5: "- Successfully deployed Data Lake (Firehose, Glue, Athena) and SNS event notification system.",
    6: "- Fully integrated AWS Cognito, secured all APIs with JWT, and finalized Backend RBAC.",
    7: "- Completed Leave Management module with complex anti-overlap checking logic and attendance event synchronization.",
    8: "- Backend system achieved production standards with X-Ray Tracing, CloudWatch Alarms, and robust SQS Buffer architecture."
}

def process_file(lang, week_num, file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    result_text = vi_results[week_num] if lang == 'vi' else en_results[week_num]
    
    # More robust regex for results replacement
    pattern = r"(## 3\..*?\n).*?(?=\n## 4\.)"
    content = re.sub(pattern, r"\1" + result_text + "\n", content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"d:\AWS\fcj-workshop-template\content\1-Worklog"
for w in range(1, 9):
    vi_path = os.path.join(base_dir, f"{w}-Week{w}", "_index.vi.md")
    en_path = os.path.join(base_dir, f"{w}-Week{w}", "_index.md")
    process_file('vi', w, vi_path)
    process_file('en', w, en_path)
    print(f"Updated results for week {w}")
