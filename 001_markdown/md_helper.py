import pyperclip

def get_highest_head_level(content):
    lines = content.split('\n')
    highest_level = float('inf')
    for line in lines:
        head_level = 0
        for char in line:
            if char == '#':
                head_level += 1
            else:
                break
        if head_level > 0 and head_level < highest_level:
            highest_level = head_level
    return highest_level

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
            new_line = '#' * new_head_level + line[head_level:]
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    return '\n'.join(new_lines)

def main():
    content = pyperclip.paste()
    highest_level = get_highest_head_level(content)
    print(f"The highest head level is {highest_level}")
    downgrade_level = int(input("Enter the number by which you want to downgrade the headers: "))
    new_content = downgrade_heads(content, downgrade_level)
    pyperclip.copy(new_content)
    print("Content updated in clipboard.")

if __name__ == "__main__":
    main()
