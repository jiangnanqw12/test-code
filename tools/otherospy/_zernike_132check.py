import os



allFileList = os.listdir()

n = 0
iLine = 0x100
iColumn = 0x100
counter=0
for file_num in range(1):
    filenameStr = "Matrix_256x256_Line0_2000_"
    f_test = open(filenameStr + str(file_num) + ".txt")
    f_ori = open("../" + str(file_num + 1) + ".txt")
    linelist_test = f_test.readlines()
    linelist_ori = f_ori.readlines()
    for line in range(256):
        line_test = linelist_test[line]
        line_data_list=line_test.split(sep=" ")
        for column in range(256):
            if (linelist_ori[line * 265 + column] != line_data_list[column]):
                counter +=1
                print("ori: ",linelist_ori[line * 265 + column])
                print("test: ",line_data_list[column])
        if counter == 0:
            print("{} pass",line)

    f_test.close
    f_ori.close
