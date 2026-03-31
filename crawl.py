import sys

# 获取你输入的课文名字
lesson = sys.argv[1]

# 正确的 Markdown 模板（保证换行和分段）
md_content = f"""# {lesson}

## 课文资料
自动收集完成

## 重点内容
待整理

## 我的理解
待补充

## 标签
#课文 #{lesson}
"""

# 保存成 .md 笔记文件
with open(f"{lesson}.md", "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"✅ 笔记已生成：{lesson}.md")
