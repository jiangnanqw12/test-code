import os
# -*- coding: UTF-8 -*-
#path = "/mnt/c/Users/shadow/Desktop/temp/"
#path = "/mnt/d/BaiduNetdiskDownload/YouTube/Understanding Kalman Filters/"
#path = "C:\\Users\\shadow\\Desktop\\temp\\"
path = os.getcwd()+"\\"
listdir = os.listdir(path)

# print(listdir)

for i in range(len(listdir)):

    filename = listdir[i]
    filenamelist = filename.split(sep=".")
    if filenamelist[-1] == "srt":

        f = open(path+filename, 'r', encoding='UTF-8')
        linelist = f.readlines()

        # print(linelist)
        f2 = open(path+filenamelist[0]+".txt", "w")
        counter = 1
        # print(linelist[i], end="")
        #print(i + 1, ":", linelist[i], end="")
        pop_idx_list = []
        for i in range(len(linelist)):
            # print(linelist[i])
            if linelist[i] == "\n":
                pop_idx_list.append(i)
                continue
            else:

                try:
                    sub_counter = int(linelist[i])
                    if (int(linelist[i]) == counter):
                        pop_idx_list.append(i)
                        counter += 1
                        continue
                    else:
                        print("error idx:", linelist[i])
                except:
                    #print("int fail:\n", linelist[i])
                    timelinelist = linelist[i].split(" ")
                    if len(timelinelist) > 2:
                        if timelinelist[1] == "-->":

                            pop_idx_list.append(i)
                            continue

        # print(pop_idx_list)
        # remove multiple data from the list
        if pop_idx_list != []:
            for index in sorted(pop_idx_list, reverse=True):
                del linelist[index]
        for line in linelist:
            if line[-2] == " ":
                if line[-3] == "." or line[-3] == "?":
                    f2.write(line+"\n")
                else:
                    f2.write(line[:-1])
            elif line[-2] == "." or line[-2] == "?":
                f2.write(line+"\n")
            else:
                f2.write(line[:-1]+" ")
                # print(1)
                # f2.write(line+"\n")
                # print(ord(line[-2]))
                # if line[-2] == "." or line[-2] == "?":
                #     print(line)
                #     f2.write(line)

                # else:
                #     f2.write(line[:-1])
        f2.close()
        f.close()
