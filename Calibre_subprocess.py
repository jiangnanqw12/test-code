import subprocess


def convert_epub_to_pdf(epub_file_path, output_pdf_path):
    try:
        # Command to convert EPUB to PDF
        command = ['ebook-convert', epub_file_path, output_pdf_path]

        # Run the command
        result = subprocess.run(command, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Output the result
        print("Conversion successful, output file created:", output_pdf_path)
        return result.stdout.decode()

    except subprocess.CalledProcessError as e:
        print("Error during conversion:", e.stderr.decode())
        return None


def main():
    # Example usage
    # Replace with the path to your .epub file
    epub_file = 'The Bullet Journal Method Track Your Past, Order Your Present, Plan Your Future.epub'
    # Replace with the desired output PDF path
    output_pdf = 'The Bullet Journal Method Track Your Past, Order Your Present, Plan Your Future.pdf'

    convert_epub_to_pdf(epub_file, output_pdf)


if __name__ == "__main__":
    main()
