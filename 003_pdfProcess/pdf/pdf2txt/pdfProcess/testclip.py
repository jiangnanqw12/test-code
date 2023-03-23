
import pyperclip
import os
#coding in utf-8
# text = pyperclip.paste()
# path = os.getcwd()+"/"
# f1=open(path+"test.txt","w")
# f1.write(text)


def copy_text_from_clip(path, end_file):
    text = pyperclip.paste()
    # print("clip:",text)
    #path = os.getcwd()+"/"
    f1 = open(path+"re."+end_file, "w", encoding="utf-8")
    f1.write(text)


if __name__ == '__main__':
    path = os.getcwd()+"/"
    copy_text_from_clip(path, "pdftext")
