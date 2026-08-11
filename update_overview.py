import os
import re

# 1. Update 5.1-Workshop-overview/_index.vi.md
with open(r"d:\AWS\fcj-workshop-template\content\2-Proposal\_index.vi.md", "r", encoding="utf-8") as f:
    prop_vi = f.read()

vi_table_match = re.search(r"(\| STT \| DỊCH VỤ AWS.*?\n\n)", prop_vi, re.DOTALL)
if vi_table_match:
    vi_table = vi_table_match.group(1).strip()
    with open(r"d:\AWS\fcj-workshop-template\content\5-Workshop\5.1-Workshop-overview\_index.vi.md", "r", encoding="utf-8") as f:
        over_vi = f.read()
    
    new_over_vi = re.sub(
        r"(### 3\. Các dịch vụ trong phạm vi  \(In-Scope Services\)\n).*?(?=\n### 4\. Kết quả mong đợi)",
        r"\g<1>\n" + vi_table + "\n",
        over_vi,
        flags=re.DOTALL
    )
    with open(r"d:\AWS\fcj-workshop-template\content\5-Workshop\5.1-Workshop-overview\_index.vi.md", "w", encoding="utf-8") as f:
        f.write(new_over_vi)

# 2. Update 5.1-Workshop-overview/_index.md
with open(r"d:\AWS\fcj-workshop-template\content\2-Proposal\_index.md", "r", encoding="utf-8") as f:
    prop_en = f.read()

en_table_match = re.search(r"(\| No\. \| AWS SERVICE.*?\n\n)", prop_en, re.DOTALL)
if en_table_match:
    en_table = en_table_match.group(1).strip()
    with open(r"d:\AWS\fcj-workshop-template\content\5-Workshop\5.1-Workshop-overview\_index.md", "r", encoding="utf-8") as f:
        over_en = f.read()
    
    new_over_en = re.sub(
        r"(### 3\. In-Scope Services\n).*?(?=\n### 4\. Expected Outcomes)",
        r"\g<1>\n" + en_table + "\n",
        over_en,
        flags=re.DOTALL
    )
    with open(r"d:\AWS\fcj-workshop-template\content\5-Workshop\5.1-Workshop-overview\_index.md", "w", encoding="utf-8") as f:
        f.write(new_over_en)


# 3. Update 5-Workshop navigation links
nav_vi = """
1. [Giới thiệu tổng quan kiến trúc](5.1-Workshop-overview/)
2. [Chuẩn bị tài nguyên (Prerequisite)](5.2-Prerequiste/)
3. [Phần 1: Cấu hình Xác thực & Bảo mật (Cognito, WAF, IAM)](5.3-Auth-Security/)
4. [Phần 2: Cấu hình Database & Lưu trữ (DynamoDB, S3)](5.4-Database-Storage/)
5. [Phần 3: Cấu hình AI & API (Rekognition, Lambda, API Gateway)](5.5-AI-API/)
6. [Phần 4: Kiến trúc Event-Driven (EventBridge, SQS, SNS/SES)](5.6-Event-Driven/)
7. [Phần 5: Data Pipeline & Analytics (Firehose, Athena)](5.7-Data-Analytics/)
8. [Phần 6: CI/CD Pipeline (CodeBuild, CodePipeline)](5.8-CI-CD-Frontend/)
9. [Phần 7: Giám sát hệ thống (CloudWatch, X-Ray)](5.9-Monitoring-Tracing/)
10. [Phần 8: Kiểm thử & Xác thực (Testing & Validation)](5.10-Testing-Validation/)
11. [Dọn dẹp tài nguyên (Clean-up)](5.11-Cleanup/)
"""

nav_en = """
1. [Architecture Overview](5.1-Workshop-overview/)
2. [Resource Preparation (Prerequisites)](5.2-Prerequiste/)
3. [Part 1: Auth & Security Configuration (Cognito, IAM)](5.3-Auth-Security/)
4. [Part 2: Database & Storage Configuration (DynamoDB, S3)](5.4-Database-Storage/)
5. [Part 3: AI & API Configuration (Rekognition, Lambda, API Gateway, WAF)](5.5-AI-API/)
6. [Part 4: Event-Driven Architecture (EventBridge, SQS, SNS, SES)](5.6-Event-Driven/)
7. [Part 5: Data Pipeline & Analytics (DataLake Worker, Glue, Athena)](5.7-Data-Analytics/)
8. [Part 6: Deployment & CI/CD Automation (Backend, S3, CloudFront, Frontend)](5.8-CI-CD-Frontend/)
9. [Part 7: Monitoring & Tracing (CloudWatch, X-Ray)](5.9-Monitoring-Tracing/)
10. [Part 8: Testing & Validation (Testing, Cleanup)](5.10-Testing-Validation/)
11. [Cleanup Resources (Clean-up)](5.11-Cleanup/)
"""

with open(r"d:\AWS\fcj-workshop-template\content\5-Workshop\_index.vi.md", "r", encoding="utf-8") as f:
    ws_vi = f.read()
ws_vi = re.sub(r"(#### Nội dung Workshop\n\n).*?(?=\Z)", r"\g<1>" + nav_vi.strip() + "\n", ws_vi, flags=re.DOTALL)
with open(r"d:\AWS\fcj-workshop-template\content\5-Workshop\_index.vi.md", "w", encoding="utf-8") as f:
    f.write(ws_vi)

with open(r"d:\AWS\fcj-workshop-template\content\5-Workshop\_index.md", "r", encoding="utf-8") as f:
    ws_en = f.read()
ws_en = re.sub(r"(#### Workshop Content\n\n).*?(?=\Z)", r"\g<1>" + nav_en.strip() + "\n", ws_en, flags=re.DOTALL)
with open(r"d:\AWS\fcj-workshop-template\content\5-Workshop\_index.md", "w", encoding="utf-8") as f:
    f.write(ws_en)

print("Update completed.")