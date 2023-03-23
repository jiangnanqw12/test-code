import os
#path = "/mnt/c/Users/shadow/Downloads/test"

# f = os.listdir(path)
f = os.listdir()
n = 0

for i in range(len(f)):



    oldname = f[i]
    filename = f[i].split(sep=".")


    # print(file[-1])
    if filename[-1] == "cpp":
        newname = filename[0]+'.c'


        os.rename(oldname, newname)
        print(oldname, '======>', newname)
