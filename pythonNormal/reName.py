import os
#path = "/mnt/c/Users/shadow/Downloads/test"

path = "C:\\BaiduNetdiskDownload\\TV版 153集"
# 获取该目录下所有文件，存入列表中
f = os.listdir(path)

n = 0

for i in range(len(f)):

    # 设置旧文件名（就是路径+文件名）

    oldname = path+"/"+f[i]
    filename = f[i].split(sep=".")

    # 设置新文件名
    # print(file[-1])
    if filename[-1] == "pdf":
        newname = path+"/"+filename[0]+'.mkv'

        # 用os模块中的rename方法对文件改名
        os.rename(oldname, newname)
        print(oldname, '======>', newname)
