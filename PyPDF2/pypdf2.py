
#from PyPDF2 import PdfFileReader, PdfFileWriter
import PyPDF2


def split(path, name_of_split):
    #pdf = PyPDF2.PdfFileReader(path)
    pdf = PyPDF2.PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = '1.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)


if __name__ == '__main__':
    path = '04-float.pdf'
    split(path, 'NO')
