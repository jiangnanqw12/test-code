import re
import os

def modify_code_block(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regular expression to match code blocks
    code_block_pattern = re.compile(r"```(.*?)```", re.DOTALL)

    def replace_code_block(match):
        code_block = match.group(1).strip()

        # If the code block starts with "cppCopy code", add "cpp" as the language identifier
        if code_block.startswith("cppCopy code"):
            code_block = "cpp\n" + code_block[len("cppCopy code"):].strip()

        return f"```{code_block}\n```"

    # Replace code blocks using the defined function
    modified_content = code_block_pattern.sub(replace_code_block, content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)

def main():
    file_list = os.listdir(os.getcwd())
    for file_name in file_list:
        if file_name.endswith('.md'):
            output_dir = os.path.join(os.getcwd(), "output")
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            output_file = os.path.join(output_dir, file_name)
            modify_code_block(file_name, output_file)
            print(file_name)

if __name__ == "__main__":
    main()
