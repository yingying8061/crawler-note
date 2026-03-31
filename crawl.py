import sys

# 1. 获取你输入的课文名字
lesson_name = sys.argv[1]

# 2. 模拟爬取到的内容（以后换成真实爬虫的结果）
crawl_content = """
《海底世界》是一篇科普性说明文。作者化身“深海导游”，带我们穿过波涛澎湃的海面，潜入宁静深邃的海底，揭开了那个景色奇异、物产丰富的神秘世界。
- 核心问题：大海深处是怎样的？
- 主要内容：从环境、动物、植物、矿产四个方面具体介绍
- 中心句：海底真是个景色奇异、物产丰富的世界！
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
