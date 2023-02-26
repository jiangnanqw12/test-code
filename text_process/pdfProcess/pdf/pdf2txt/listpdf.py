import os
from pdfProcess import list_reform
from pdfProcess import testclip

if __name__ == '__main__':
    path = os.getcwd()+"/"
    testclip.copy_text_from_clip(path, "txtlist")
    list_reform.list_reform(path)