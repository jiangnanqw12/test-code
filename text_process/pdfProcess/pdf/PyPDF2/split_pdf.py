from PyPDF2 import PdfFileWriter, PdfFileReader
import os
path = os.getcwd()+"/"


def split_pdf_fix_range(path4pdf):
    for (dirpath, dirnames, filenames) in os.walk(path4pdf):
        if filenames != []:
            for filename in filenames:
                filenamelist = filename.split(".")
                if filenamelist[-1] == "pdf":
                    os.mkdir(filenamelist[0])
                    inputpdf = PdfFileReader(open(dirpath+filename, "rb"))
                    for i in range(inputpdf.numPages):
                        output = PdfFileWriter()
                        output.addPage(inputpdf.getPage(i))

                        with open(dirpath+"/"+filenamelist[0]+"/"+filenamelist[0]+"_split_"+"page_%s.pdf" % (i+1), "wb") as fp:
                            output.write(fp)


split_pdf_fix_range(path)

# os.mkdir("test")
