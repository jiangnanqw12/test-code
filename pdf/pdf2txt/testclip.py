
import pyperclip
import os
# text = pyperclip.paste()
# path = os.getcwd()+"/"
# f1=open(path+"test.txt","w")
# f1.write(text)
def copy_text_from_clip(path,end_file):
    text = pyperclip.paste()
    #path = os.getcwd()+"/"
    f1=open(path+"re."+end_file,"w")
    f1.write(text)