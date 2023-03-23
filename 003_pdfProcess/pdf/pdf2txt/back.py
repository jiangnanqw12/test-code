
import os
from pdfProcess import testclip
from pdfProcess import pdf2txt
from pdfProcess import text_replace
if __name__ == '__main__':
    idx = input("copy process plz input 1")
    path = os.getcwd()+"/"
    if idx == "1":

        testclip.copy_text_from_clip(path, "pdftext")
        pdf2txt.pdf2text(path)
        text_replace.text_replace(path)
