import os
#coding in utf-8
#提取pdf复制出来的list文字，进行纯文字输出
path = os.getcwd()+"/"
listdir = os.listdir(path)
for i in range(len(listdir)):

    filename = listdir[i]
    filenamelist = filename.split(sep=".")
    if filenamelist[-1] == "txtlist":

        f = open(path+filename, 'r', encoding='UTF-8')
        linelist = f.readlines()

        # print(linelist)
        f2 = open(path+filenamelist[0]+".txtlist2", "w")
        for i in range(len(linelist)):
            #print(linelist[i][-1])
            list4remove=[" ","• "," ","– "]
            flag=0
            for j in (range(len(list4remove))):
                if linelist[i].find(list4remove[j]) !=-1:
                    f2.write(linelist[i][2:]+"\n")
                    flag=1

            if flag==0:
                f2.write(linelist[i]+"\n")


