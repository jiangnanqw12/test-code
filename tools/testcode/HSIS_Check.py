import os



allFileList = os.listdir()

n = 0

for i in range(len(allFileList)):



    fileName = allFileList[i]
    fileList = allFileList[i].split(sep=".")

    # 设置新文件名
    # print(file[-1])
    if fileList[-1] == "txt":
        fileNameList=fileList[0].split(sep="_")
        if(fileNameList[0]=="HSIS"):
            #print(fileNameList[-1])
            f = open(fileName)
            f2 = open("origin/" + "solution_" + fileName)
            lineList = f.readlines()
            lineList2 = f2.readlines()
            count=0
            for i in range(len(lineList)):
                if lineList[i] != lineList2[i]:
                    #print("error", fileName,"line:",i)
                    count += 1
            if count==0:
                print(fileName, " pass")
            else:
                print(fileName, " failed")
            f.close
            f2.close
