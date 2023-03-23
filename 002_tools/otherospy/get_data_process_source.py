import os
def get_data_process_source(order):
    #0 int
    #1 SMEE_UINT32
    # path = ""
    # listfiles = os.listdir()
    f2 = open("_data_process.c", "wb")

    f2.write(b"#include \"FRTP_BaseType.h\"\n")
    f2.write(b"#include \"FRTP_Api_if.h\"\n")
    f2.write(b"#include \"zernike_process.h\"\n")
    if order:
        f2.write(b"extern SMEE_UINT32 *zernike_ptr[];\n")
    else:
        f2.write(b"extern int *zernike_ptr[];\n")
    for i in range(77):
        if order:
            f2.write(b"extern SMEE_UINT32 ")
        else:
            f2.write(b"extern int ")
        f2.write(b"zernike0")
        if i < 9:
            f2.write(b"0")
        ib2 = bytes(str(i+1), encoding="utf8")
        f2.write(ib2)
        f2.write(b"[];\n")
    if order:
        f2.write(b"SMEE_UINT32 init_zernike_ptr()\n{\n")
    else:
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
    f2.write(b"return;\n")
    f2.write(b"}\n")


