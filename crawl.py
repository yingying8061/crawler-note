import sys

# 1. 获取你输入的课文名字
lesson_name = sys.argv[1]

# 2. 空占位符：以后爬什么课文，就填什么内容
crawl_content = f"""
《{lesson_name}》是一篇课文。

- **核心问题**：
- **主要内容**：
- **中心句**：
"""

# 3. 读取你预先写好的「学霸模板」
with open("lesson_template.md", "r", encoding="utf-8") as f:
    template = f.read()

# 4. 自动替换模板里的变量
final_note = template.format(
    lesson_name=lesson_name,
    crawl_content=crawl_content
)

# 5. 生成最终笔记文件
with open(f"{lesson_name}_学霸笔记.md", "w", encoding="utf-8") as f:
    f.write(final_note)

print(f"✅ 学霸笔记已生成：{lesson_name}_学霸笔记.md")
