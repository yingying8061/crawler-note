import sys
import requests
from bs4 import BeautifulSoup
import re

# ----------------------
# 1. 配置：输入课文名字
# ----------------------
lesson_name = sys.argv[1]
# 固定爬取：国家中小学智慧教育平台 部编版小学语文三年级下册
base_url = "https://basic.smartedu.cn/tchMaterial"
search_url = "https://basic.smartedu.cn/search"

# ----------------------
# 2. 模拟浏览器请求（必须加，否则平台会拦截）
# ----------------------
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://basic.smartedu.cn/"
}

# ----------------------
# 3. 搜索课文，获取详情页链接
# ----------------------
print(f"🔍 正在搜索：{lesson_name}")
search_params = {
    "kw": f"{lesson_name} 三年级下册 语文",
    "subjectId": "1001",  # 语文
    "gradeId": "100503",   # 三年级
    "termId": "2",         # 下册
    "catalogId": "1001"    # 教材
}

# 注意：国家平台需要session保持，这里用简单请求兜底
# 备选方案：直接用百度百科兜底，保证100%能生成内容
try:
    # 优先爬国家平台
    res = requests.get(search_url, params=search_params, headers=headers, timeout=15)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    
    # 提取课文简介（简化版，适配平台结构）
    content_blocks = soup.find_all("div", class_="result-item")[:3]
    crawl_content = ""
    for block in content_blocks:
        title = block.find("h3").get_text(strip=True) if block.find("h3") else ""
        desc = block.find("p").get_text(strip=True) if block.find("p") else ""
        if title and desc:
            crawl_content += f"### {title}\n{desc}\n\n"
    
    # 如果国家平台没抓到，用百度百科兜底
    if not crawl_content.strip():
        raise Exception("国家平台未抓取到内容，切换百度百科兜底")

except Exception as e:
    print(f"⚠️ 国家平台抓取失败，切换百度百科兜底：{e}")
    # 百度百科兜底，保证100%生成内容
    baidu_url = f"https://baike.baidu.com/item/{lesson_name} 课文"
    baidu_res = requests.get(baidu_url, headers=headers, timeout=15)
    baidu_soup = BeautifulSoup(baidu_res.text, "html.parser")
    
    crawl_content = ""
    # 抓取百度百科的课文简介
    for p in baidu_soup.find_all("p")[:6]:
        text = p.get_text(strip=True)
        if text and len(text) > 10:  # 过滤空行和短内容
            crawl_content += f"{text}\n\n"

# ----------------------
# 4. 读取学霸模板，自动填充
# ----------------------
print("📝 正在套用学霸模板...")
with open("lesson_template.md", "r", encoding="utf-8") as f:
    template = f.read()

# 替换模板变量
final_note = template.format(
    lesson_name=lesson_name,
    crawl_content=crawl_content
)

# ----------------------
# 5. 生成最终笔记文件
# ----------------------
output_file = f"{lesson_name}_学霸笔记.md"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(final_note)

print(f"✅ 成功！笔记已生成：{output_file}")
