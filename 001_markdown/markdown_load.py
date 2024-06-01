from markdown_it import MarkdownIt
from markdown_it.token import Token

def parse_markdown(md_text):
    md = MarkdownIt()
    tokens = md.parse(md_text)

    titles = []
    bull_list = []

    def process_tokens(tokens, parent_level=0):
        current_level = parent_level
        for token in tokens:
            if token.type.startswith('heading'):
                level = int(token.tag[1])
                titles.append((level, token.content))
            elif token.type == 'list_item_open':
                current_level += 1
            elif token.type == 'list_item_close':
                current_level -= 1
            elif token.type == 'inline' and current_level > 0:
                bull_list.append((current_level, token.content))
            if token.children:
                process_tokens(token.children, current_level)

    process_tokens(tokens)
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
    print(f"Level {level}: {title}")

print("\nBullet List:")
for level, item in bull_list:
    print(f"Level {level}: {item}")
