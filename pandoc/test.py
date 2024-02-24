import os
import subprocess


def convert_md_to_pdf(md_file, pdf_file, template_file):
    command = [
        'pandoc',
        md_file,
        '-o',
        pdf_file,
        '--template',
        template_file,
        '--pdf-engine',
        # Use double backslashes for Windows paths
        'C:\\Program Files\\MiKTeX\\miktex\\bin\\x64\\pdflatex.exe'
    ]
    try:
        subprocess.run(command, check=True)
        print(f"Successfully converted {md_file} to {pdf_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":

    cwd = os.getcwd()
    input_file = os.path.join(cwd, 'jianli.md')
    convert_md_to_pdf(input_file, 'output.pdf', 'custom-template.tex')
