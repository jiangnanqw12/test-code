import os
# listfiles = os.listdir()
# print(listfiles)
mypath = ""
f = []

for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    #print (dirpath)
    #print (dirnames)
    #print (filenames)
    # f.extend(filenames)
    if filenames != []:

        for filename in filenames:
            filenamelist = filename.split(".")
            if filenamelist[-1] == "vtt":
                #print (filename)
                #print (dirpath)
                path = dirpath+"/"
                f = open(path + filename, "r")
                try:
                    linelist = f.readlines()

                except:
                    print(dirpath)
                    print(filename)
                    # break
                # print(linelist)
                f2 = open(path+filenamelist[0] +
                          filenamelist[1]+filenamelist[2]+".txt", "w")
                counter = 0
                # print(linelist[i], end="")
                #print(i + 1, ":", linelist[i], end="")

                for i in range(len(linelist)):
                    if ((i + 1) % 3 == 0):
                        pos4end = 2

                        line = linelist[i]

                        if line != [] or line != "\n\r":
                            try:
                                if line[-pos4end] == ".":

                                    f2.write(line)
                                    f2.write("\n")
                                else:
                                    if line[0:-2] == "Language: en":
                                        pass
                                    else:
                                        f2.write(line[0:-2]+" ")
                            except:
                                #print("error", line)
                                pass

                            counter += 1
                # print(counter)
                # print(len(linelist))
                # if counter * 3 != len(linelist)-1:
                #     print("errors")
                f2.close()

                f.close()


# print(f)
