import markdown
from bs4 import BeautifulSoup

def parse_markdown(md_text):
    # 将Markdown文本转换为HTML
    html = markdown.markdown(md_text)
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html, 'html.parser')

    # 提取标题和列表项
    titles = []
    bull_list = []

    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        titles.append((tag.name, tag.get_text()))

    def extract_list_items(soup, parent_level=0):
        for ul in soup.find_all('ul', recursive=False):
            level = parent_level + 1
            for li in ul.find_all('li', recursive=False):
                bull_list.append((level, li.get_text(strip=True)))
                extract_list_items(li, level)

    extract_list_items(soup)

    return titles, bull_list

markdown_text = """
# 一级标题
- 一级项目 1
  - 二级项目 1.1
  - 二级项目 1.2
    - 三级项目 1.2.1
## 二级标题
- 一级项目 2
  - 二级项目 2.1
  - 二级项目 2.2
"""

titles, bull_list = parse_markdown(markdown_text)

print("Titles:")
for level, title in titles:
    print(f"{level}: {title}")

print("\nBullet List:")
for level, item in bull_list:
    print(f"Level {level}: {item}")
