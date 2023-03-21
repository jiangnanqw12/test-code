import cairosvg
import os

def convert_pdf_to_svg(pdf_path, output_dir, file_prefix=""):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(pdf_path, "rb") as pdf_file:
        try:
            num_pages = cairosvg.pdf.get_page_count(pdf_file)
            pdf_file.seek(0)

            for page_num in range(num_pages):
                svg_output_path = os.path.join(output_dir, f"{file_prefix}page_{page_num + 1}.svg")
                cairosvg.pdf2svg(url=pdf_path, write_to=svg_output_path, dpi=72, file_obj=pdf_file, page_index=page_num)
        except Exception as e:
            print(f"Error converting PDF to SVG: {e}")
def current_folder_pdf_2_svg():
    file_list=os.listdir(os.path.abspath(os.curdir))
    for file in file_list:
        if file.endswith('.pdf'):
            convert_pdf_to_svg(file, file[:-4], file_prefix="converted_")
def test1():
    input_pdf = "input.pdf"
    output_directory = "output_svgs"
    convert_pdf_to_svg(input_pdf, output_directory, file_prefix="converted_")
if __name__ == "__main__":
    current_folder_pdf_2_svg()
