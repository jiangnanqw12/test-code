import os
path = ""
listfiles = os.listdir()
f2 = open("_data.h", "wb")
f2.write(b"#ifndef ")
f2.write(b"_DATA_H"+b"\n")

f2.write(b"#define ")
f2.write(b"_DATA_H"+b"\n")

f2.write(b"#include \"FRTP_BaseType.h\"\n")
f2.write(b"#include \"FRTP_Api_if.h\"\n")
for i in range(len(listfiles)):
    filename = listfiles[i]
    filenamelist = filename.split(sep=".")
    if filenamelist[-1] == "h":
        fb = bytes(filename, encoding="utf8")
        f2.write(b"#include \"")
        f2.write(fb )
        f2.write(b"\"\n")
f2.write(b"#endif //")
f2.write(b"_DATA_H"+b"\n")

