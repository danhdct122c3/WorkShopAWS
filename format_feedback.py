import os
import re

def reformat_content(content, lang):
    # Remove all horizontal rules completely except the one separating the frontmatter
    # The frontmatter has two '---'. We want to keep them.
    # Split by the second '---'
    parts = content.split('---', 2)
    if len(parts) >= 3:
        frontmatter = parts[0] + '---' + parts[1] + '---'
        body = parts[2]
    else:
        frontmatter = ""
        body = content

    # Remove horizontal rules in body
    body = re.sub(r'\n---\n', '\n\n', body)
    
    # Replace '### 1.' to inject '## Đánh giá chung'
    if lang == 'vi':
        body = re.sub(r'### 1\. (.*)', r'## Đánh giá chung\n\n**1. \1**', body)
        body = re.sub(r'### Câu hỏi thêm', r'## Cảm nhận cá nhân sau quá trình thực tập', body)
        body = re.sub(r'### Đề xuất & mong muốn', r'## Đề xuất & mong muốn', body)
    else:
        body = re.sub(r'### 1\. (.*)', r'## Overall Assessment\n\n**1. \1**', body)
        body = re.sub(r'### Additional Questions', r'## Personal Reflections after the Internship', body)
        body = re.sub(r'### Suggestions & Expectations', r'## Suggestions & Expectations', body)
    
    # Replace other '### X.' with bold
    body = re.sub(r'### (\d+\..*)', r'**\1**', body)
    
    # Clean up excessive newlines
    body = re.sub(r'\n{3,}', '\n\n', body)
    
    return frontmatter + body

base_dir = r"d:\AWS\fcj-workshop-template\content\7-Feedback"

vi_path = os.path.join(base_dir, "_index.vi.md")
with open(vi_path, 'r', encoding='utf-8') as f:
    vi_content = f.read()
with open(vi_path, 'w', encoding='utf-8') as f:
    f.write(reformat_content(vi_content, 'vi'))

en_path = os.path.join(base_dir, "_index.md")
with open(en_path, 'r', encoding='utf-8') as f:
    en_content = f.read()
with open(en_path, 'w', encoding='utf-8') as f:
    f.write(reformat_content(en_content, 'en'))

print("Formatting updated.")