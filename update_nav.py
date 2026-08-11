import os
import re

folders = [
    "5.1-Workshop-overview",
    "5.2-Prerequiste",
    "5.3-Auth-Security",
    "5.4-Database-Storage",
    "5.5-AI-API",
    "5.6-Event-Driven",
    "5.7-Data-Analytics",
    "5.8-CI-CD-Frontend",
    "5.9-Monitoring-Tracing",
    "5.10-Testing-Validation",
    "5.11-Cleanup"
]

base_dir = r"d:\AWS\fcj-workshop-template\content\5-Workshop"

def get_title(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Match title in frontmatter
    match = re.search(r'^title\s*:\s*"?([^"\n]+)"?', content, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        return title
    return None

nav_vi_lines = []
nav_en_lines = []

for i, folder in enumerate(folders, 1):
    vi_path = os.path.join(base_dir, folder, "_index.vi.md")
    en_path = os.path.join(base_dir, folder, "_index.md")
    
    vi_title = get_title(vi_path)
    en_title = get_title(en_path)
    
    if not vi_title: vi_title = folder
    if not en_title: en_title = folder
    
    nav_vi_lines.append(f"{i}. [{vi_title}]({folder}/)")
    nav_en_lines.append(f"{i}. [{en_title}]({folder}/)")

nav_vi_text = "\n".join(nav_vi_lines)
nav_en_text = "\n".join(nav_en_lines)

# Replace in _index.vi.md
with open(os.path.join(base_dir, "_index.vi.md"), "r", encoding="utf-8") as f:
    ws_vi = f.read()
ws_vi = re.sub(r"(#### Nội dung Workshop\n\n).*?(?=\Z)", r"\g<1>" + nav_vi_text + "\n", ws_vi, flags=re.DOTALL)
with open(os.path.join(base_dir, "_index.vi.md"), "w", encoding="utf-8") as f:
    f.write(ws_vi)

# Replace in _index.md
with open(os.path.join(base_dir, "_index.md"), "r", encoding="utf-8") as f:
    ws_en = f.read()
ws_en = re.sub(r"(#### Workshop Content\n\n).*?(?=\Z)", r"\g<1>" + nav_en_text + "\n", ws_en, flags=re.DOTALL)
with open(os.path.join(base_dir, "_index.md"), "w", encoding="utf-8") as f:
    f.write(ws_en)

print("Updated titles:")
print(nav_vi_text)
print("---")
print(nav_en_text)