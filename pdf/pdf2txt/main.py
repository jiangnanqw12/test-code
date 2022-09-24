
import os
from pdfProcess import testclip
from pdfProcess import pdf2txt
from pdfProcess import text_replace
from pdfProcess import read_replace_list
if __name__ == '__main__':

    path = os.getcwd()+"/"

    testclip.copy_text_from_clip(path, "pdftext")
    pdf2txt.pdf2text(path)
    # replace_list=[]
    # read_replace_list.read_replace_list(path,replace_list)
    text_replace.text_replace(path)
