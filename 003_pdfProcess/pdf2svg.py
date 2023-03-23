import cairosvg
import os

import os
import subprocess

def convert_pdf_to_svg(pdf_path, output_dir, file_prefix=""):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf_name, _ = os.path.splitext(os.path.basename(pdf_path))
    temp_svg_path = os.path.join(output_dir, f"{pdf_name}_temp.svg")

    try:
        subprocess.run(["pdf2svg", pdf_path, temp_svg_path], check=True)

        with open(temp_svg_path, "r") as temp_svg_file:
            svg_content = temp_svg_file.read()

        os.remove(temp_svg_path)

        # Replace the id of the first svg element to avoid conflicts with other SVGs
        new_svg_id = f"{file_prefix}{pdf_name}"
        svg_content = svg_content.replace('id="svg1"', f'id="{new_svg_id}"')

        svg_output_path = os.path.join(output_dir, f"{file_prefix}{pdf_name}.svg")
        with open(svg_output_path, "w") as svg_output_file:
            svg_output_file.write(svg_content)

    except Exception as e:
        print(f"Error converting PDF to SVG: {e}")



def current_folder_pdf_2_svg():
    file_list=os.listdir(os.path.abspath(os.curdir))
    for file in file_list:
        if file.endswith('.pdf'):
            convert_pdf_to_svg(file, os.getcwd(), file_prefix="converted_")
def test1():
    input_pdf = "input.pdf"
    output_directory = "output_svgs"
    convert_pdf_to_svg(input_pdf, output_directory, file_prefix="converted_")
if __name__ == "__main__":
    current_folder_pdf_2_svg()
