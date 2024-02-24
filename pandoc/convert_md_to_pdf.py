import os
import re
import subprocess


def contains_chinese(text):
    """Check if the text contains Chinese characters."""
    return any('\u4e00' <= char <= '\u9fff' for char in text)


def convert_md_to_pdf(md_file, pdf_file, template_file=None):
    # Read the content of the Markdown file
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Check if the content contains Chinese characters
    if contains_chinese(content):
        print("The document contains Chinese characters.")
        # Use xelatex for Chinese character support
        pdf_engine = 'xelatex'
        if template_file is None:
            template_file = 'custom-template_cn.tex'
    else:
        print("The document does not contain Chinese characters.")
        # Use pdflatex if no Chinese characters are present
        pdf_engine = 'C:\\Program Files\\MiKTeX\\miktex\\bin\\x64\\pdflatex.exe'
        if template_file is None:
            template_file = 'custom-template.tex'

    command = [
        'pandoc',
        md_file,
        '-o',
        pdf_file,
        '--template',
        template_file,
        '--pdf-engine',
        pdf_engine
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Successfully converted {md_file} to {pdf_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    cwd = os.getcwd()
    input_file = os.path.join(cwd, 'jianli.md')
    convert_md_to_pdf(input_file, 'output.pdf')
