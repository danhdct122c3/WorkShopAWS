import os
import re

base_dir = r"d:\AWS\fcj-workshop-template\content\1-Worklog"
for w in range(1, 9):
    for lang in ['vi', 'en']:
        file_path = os.path.join(base_dir, f"{w}-Week{w}", "_index.vi.md" if lang == 'vi' else "_index.md")
        if not os.path.exists(file_path):
            continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find the index of "## 4. "
        idx = content.find("## 4. ")
        if idx != -1:
            new_content = content[:idx].rstrip() + "\n"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Truncated section 4 in Week {w} ({lang})")
