import os
path = ""
listfiles = os.listdir()
for i in range(len(listfiles)):
    filename = listfiles[i]
    f = open(path+filename,"rb")
    linelist = f.readlines()
    filenamelist = filename.split(sep=".")
    if filenamelist[-1] == "txt":
        # print(linelist)
        f2 = open(path+filenamelist[0]+"_data"+".txt", "wb")
        counter = 0
        f2.write(b"{")
        for i in range(len(linelist)):

            f2.write(linelist[i])
            if i!= (len(linelist)-1):
                f2.write(b",")
        f2.write(b"}")
        f2.close()
        f.close()
