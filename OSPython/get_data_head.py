import os
path = ""
listfiles = os.listdir()

for i in range(len(listfiles)):
    filename = listfiles[i]

    filenamelist = filename.split(sep=".")
    if filenamelist[-1] == "txt":
        f = open(path+filename,"rb")
        linelist = f.readlines()
        # print(linelist)
        #f2 = open(path+filenamelist[0]+"_data"+".txt", "wb")
        #f2 = open("_data"+".txt", "wb")
        frontfile = filenamelist[0].split(sep="_")

        n = frontfile[-1]
        nb=bytes(n,encoding="utf8")
        f2 = open("_data" + n + ".h", "wb")
        f2.write(b"#ifndef ")
        f2.write(b"_DATA" + nb + b"_H"+b"\n")

        f2.write(b"#define ")
        f2.write(b"_DATA" + nb+ b"_H" + b"\n")

        f2.write(b"#include \"FRTP_BaseType.h\"\n")
        f2.write(b"#include \"FRTP_Api_if.h\"\n")
        f2.write(b"#include \"zernike_process.h\"\n")
        f2.write(b"PRAGMA_DATA_SECTION(zernike")

        f2.write(nb)
        f2.write(b", \".far:Frtp:Api:SDDR\");\n")
        #f2.write(b"PRAGMA_DATA_SECTION(zernike3, \".far:Frtp:Api:SDDR\");\n")
        #f2.write(b"int zernike3[] ={")
        f2.write(b"int zernike")
        f2.write(nb)
        f2.write(b"[] ={")
        for i in range(len(linelist)):

            f2.write(linelist[i])
            if i!= (len(linelist)-1):
                f2.write(b",")
        f2.write(b"};\n")

        # f2.write(b"zernike_ptr[")
        # f2.write(nb)
        # f2.write(b"-1]=zernike")
        # f2.write(nb)
        # f2.write(b";\n")
        f2.write(b"#endif //")
        f2.write(b"_DATA"+ nb+ b"_H"+ b"\n")
        f2.close()
        f.close()
