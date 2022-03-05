import os
def get_data_process():
    path = ""
    listfiles = os.listdir()
    f2 = open("_data_process.h", "wb")
    f2.write(b"#ifndef ")
    f2.write(b"_DATA_PROCESS_H"+b"\n")

    f2.write(b"#define ")
    f2.write(b"_DATA_PROCESS_H"+b"\n")
    f2.write(b"#include \"_data.h\"\n")
    f2.write(b"#include \"FRTP_BaseType.h\"\n")
    f2.write(b"#include \"FRTP_Api_if.h\"\n")
    f2.write(b"#include \"zernike_process.h\"\n")

    f2.write(b"int init_zernike_ptr()\n{\n")
    for i in range(77):
        f2.write(b"zernike_ptr[")
        ib = bytes(str(i), encoding="utf8")
        f2.write(ib)
        f2.write(b"] = zernike0")
        if i < 9:
            f2.write(b"0")
        ib2 = bytes(str(i+1), encoding="utf8")
        f2.write(ib2)
        f2.write(b";\n")
    f2.write(b"}\n")
    f2.write(b"#endif //")
    f2.write(b"_DATA_PROCESS_H"+b"\n")

