# getdatafromzimu

import os
# path = "D:\\BaiduNetdiskDownload\\6.00.1x Introduction to Computer Science and Programming Using Python\\week1\\1 INTRODUCTION"
path = "/mnt/d/BaiduNetdiskDownload/6.00.1x Introduction to Computer Science and Programming Using Python/week1/1 INTRODUCTION/"

listdir = os.listdir(path)
# print(listdir)
for i in range(len(listdir)):
    filename = listdir[i]
    filenamelist = filename.split(sep=".")
    if filenamelist[-1] == "srt":

        f = open(path+filename)
        linelist = f.readlines()
        # print(linelist)
        f2 = open(path+filenamelist[0]+".txt", "w")
        counter = 0
        # print(linelist[i], end="")
        #print(i + 1, ":", linelist[i], end="")
        for i in range(len(linelist)):
            if ((i + 1) % 4 == 3):
                print(linelist[i], end="")
                f2.write(linelist[i])
                counter += 1
        print(counter)
        print(len(linelist))
        if counter * 4 != len(linelist):
            print("errors")
        f2.close()
        f.close()
