import os
from pydoc import replace
#import pyperclip

#coding in utf-8


def read_replace_list(path,replace_list):
    f = open(path+"record4replace", 'r', encoding='UTF-8')
    linelist = f.readlines()
    for i in range(len(linelist)):
        if linelist[i]!="\n":
            if (i+1)%2==1:
                line=[]
                line.append(linelist[i][:-1])
            else:

                line.append(linelist[i][:-1])
                replace_list.append(line)
    print(replace_list)
if __name__ == '__main__':
    path = os.getcwd()+"/"
    replace_list=[]
    read_replace_list(path,replace_list)
    print(replace_list)