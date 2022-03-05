import os



f = os.listdir()

n = 0

for i in range(len(f)):



    oldname = f[i]
    fileList = f[i].split(sep=".")

    # 设置新文件名
    # print(file[-1])
    if fileList[-1] == "txt":
        fileNameList=fileList[0].split(sep="_")
        if(fileNameList[0]=="HSIS"):
            print(fileNameList[-1])
            newname = "solution_" + oldname
            os.rename(oldname, newname)
            print(oldname, '======>', newname)

