import pyperclip

import re


def get_highest_head_level(content):
    lines = content.split('\n')
    lowest_level = float('inf')
    pattern = re.compile(r"^(#{1,}) ")

    for line in lines:
        match = pattern.match(line)
        if match:
            level = len(match.group(1))
            if level < lowest_level:
                lowest_level = level

    return lowest_level if lowest_level != float('inf') else None

# def get_highest_head_level(content):
#     lines = content.split('\n')
#     highest_level = float('inf')
#     reg_string=[r"^(#{1,}) .+",r'\1']
#     for line in lines:
#         match=line.search(reg_string[0])
#         if match:
#             line.count("#")

#     return highest_level


def downgrade_heads(content, downgrade_level):
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        head_level = 0
        for char in line:
            if char == '#':
                head_level += 1
            else:
                break
        if head_level > 0:
            new_head_level = head_level + downgrade_level
            if new_head_level > 6:
                new_head_level = 6
            new_line = '#' * new_head_level + line[head_level:]
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    return '\n'.join(new_lines)


def retrieve_document_summary_info(content=None):
    if content is None:

        content = pyperclip.paste()
    reg_string1 = [
        r'(#{1,6}) (.+)\n\n<video src="file://.+" controls></video>\n\n- .+', r"\1# \2"]
    match = re.search(reg_string1[0], content)
    if match:
        content = re.sub(reg_string1[0], reg_string1[1], content)
    reg_string2 = [r'\n{3,}', r'\n\n']
    content = re.sub(reg_string2[0], reg_string2[1], content)
    pyperclip.copy(content)


def main():
    content = pyperclip.paste()
    highest_level = get_highest_head_level(content)
    print(f"The highest head level is {highest_level}")
    downgrade_level = int(
        input("Enter the number by which you want to downgrade the headers: "))
    new_content = downgrade_heads(content, downgrade_level)
    pyperclip.copy(new_content)
    print("Content updated in clipboard.")


if __name__ == "__main__":
    main()
