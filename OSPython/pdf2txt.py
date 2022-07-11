import os
#coding in utf-8

path = os.getcwd()+"/"
listdir = os.listdir(path)
for i in range(len(listdir)):

    filename = listdir[i]
    filenamelist = filename.split(sep=".")
    if filenamelist[-1] == "pdfp":

        f = open(path+filename, 'r', encoding='UTF-8')
        linelist = f.readlines()

        # print(linelist)
        f2 = open(path+filenamelist[0]+".pdfp2", "w")
        for i in range(len(linelist)):
            #print(linelist[i][-1])
            if i==(len(linelist)-1):
                f2.write(linelist[i])
            else:
                f2.write(linelist[i][:-1])
