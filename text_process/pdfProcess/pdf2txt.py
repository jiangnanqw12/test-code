import os
from pdfProcess import testclip
#coding in utf-8
# 提取pdf复制出来的问题，去掉换行符，加入空格


def pdf2text(path):
    listdir = os.listdir(path)
    for i in range(len(listdir)):

        filename = listdir[i]
        filenamelist = filename.split(sep=".")
        if filenamelist[-1] == "pdftext":

            f = open(path+filename, 'r', encoding='UTF-8')
            linelist = f.readlines()

            # print(linelist)
            f2 = open(path+filenamelist[0]+".pdftext2", "w", encoding='UTF-8')
            for i in range(len(linelist)):
                if linelist[i] not in ["\n", "\r\n", ""]:
                    # print(linelist[i][-1])
                    # print("-1:",linelist[i][-1])

                    # if(linelist[i][-1] == "\n"):
                    #     print("\\n\n")
                    # elif(linelist[i][-1] == "\r\n"):
                    #     print("rn\n")
                    # try:
                    #     print("-2:", linelist[i][-2])
                    # except:
                    #     print("error line:", linelist[i])

                    if linelist[i][-1] == "\n":
                        # print("\\n\n")
                        if linelist[i][-2] in [":", ".", "!", "?"]:
                            f2.write(linelist[i])
                        else:
                            f2.write(linelist[i][:-1]+" ")
                    elif linelist[i][-1] == "\r\n":
                        print("rn\n")
                    else:
                        f2.write(linelist[i]+" ")

                    #     f2.write(linelist[i]+" ")
                    # else:
                    #     f2.write(linelist[i][:-1]+" ")
if __name__ == '__main__':
    path = os.getcwd()+"/"
    testclip.copy_text_from_clip(path, "pdftext")
    pdf2text(path)
