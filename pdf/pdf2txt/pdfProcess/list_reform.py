import os
#import pyperclip
from pdfProcess import testclip
#coding in utf-8
# 提取pdf复制出来的list文字，进行纯文字输出

# def copy_text_from_clip(path):
#     text = pyperclip.paste()
#     #path = os.getcwd()+"/"
#     f1=open(path+"re.txtlist","w")
#     f1.write(text)


def list_reform(path):
    listdir = os.listdir(path)
    for i in range(len(listdir)):

        filename = listdir[i]
        filenamelist = filename.split(sep=".")
        if filenamelist[-1] == "txtlist":

            f = open(path+filename, 'r', encoding='UTF-8')
            linelist = f.readlines()

            # print(linelist)
            f2 = open(path+filenamelist[0]+".txtlist2", "w", encoding='UTF-8')
            for i in range(len(linelist)):
                # print(linelist[i][-1])
                list4remove = [" ", "• ", " ", "– "]
                flag = 0
                for j in (range(len(list4remove))):
                    if linelist[i].find(list4remove[j]) != -1:
                        f2.write(linelist[i][2:]+"\n"+"\n")
                        flag = 1

                if flag == 0:
                    f2.write(linelist[i]+"\n"+"\n")


if __name__ == '__main__':
    path = os.getcwd()+"/"
    testclip.copy_text_from_clip(path, "txtlist")
    list_reform(path)
