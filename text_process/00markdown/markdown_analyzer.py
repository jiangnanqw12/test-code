import os
import re

def read_markdown_file(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        return file.readlines()

def is_heading(line):
    match = re.match(r'^(#+)\s', line)
    if match:
        return len(match.group(1))
    return None

def is_list_item(line):
    match = re.match(r'^(\s*[-*+])\s', line)
    if match:
        return len(match.group(1).replace(' ', '')) - 1
    return None

def is_markdown_link(line):
    return re.search(r'\[(.*?)\]\((.*?)\)', line) is not None
def is_markdown_link_show(line):
    return re.search(r'!\[(.*?)\]\((.*?)\)', line) is not None
def is_markdown_link_begin(line):
    return re.search(r'^\[(.*?)\]\((.*?)\)', line) is not None
def is_markdown_link_show_begin(line):
    return re.search(r'^!\[(.*?)\]\((.*?)\)', line) is not None
def is_wiki_link(line):
    return re.search(r'\[\[(.*?)\]\]', line) is not None
def is_wiki_link_show(line):
    return re.search(r'!\[\[(.*?)\]\]', line) is not None
def is_wiki_link_begin(line):
    return re.search(r'^\[\[(.*?)\]\]', line) is not None
def is_wiki_link_show_begin(line):
    return re.search(r'^!\[\[(.*?)\]\]', line) is not None
def downgrade_headings(line):
    match = re.match(r'^(#+)\s', line)
    if match:
        return f"{match.group(1)}#{line}"
    return line
def process_markdown(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File '{file_name}' does not exist")

    lines = read_markdown_file(file_name)

    for line in lines:
        heading_level = is_heading(line)
        if heading_level:
            print(f'Heading level {heading_level}: {line.strip()}')

        list_level = is_list_item(line)
        if list_level is not None:
            print(f'List level {list_level}: {line.strip()}')

        if is_markdown_link(line):
            print(f'Markdown link: {line.strip()}')

        if is_wiki_link(line):
            print(f'Wiki link: {line.strip()}')

if __name__ == '__main__':
    try:
        process_markdown('000_O 数理科学、化学_现有笔记 1.md')
    except FileNotFoundError as e:
        print(e)
