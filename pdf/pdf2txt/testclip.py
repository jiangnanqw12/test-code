from importlib.resources import path
import pyperclip
import os
text = pyperclip.paste()
path = os.getcwd()+"/"
f1=open(path+"test.txt","w")
f1.write(text)