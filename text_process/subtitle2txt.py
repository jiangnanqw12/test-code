import os
path = os.getcwd()+"\\"
#path = "/mnt/d/BaiduNetdiskDownload/01-03 Dual Photography Videos/"
str_name_subtitle = "srt"
pos4end = -2


def line_check_if_full_sentence(line, pos4end, f):
    if line != []:
        try:
            line[pos4end]
        except:
            print(line, "in pos", pos4end, "out of range")
        if line[pos4end] in [":", "!", "?", "."]:

            f.write(line)
            f.write("\n")
        else:
            if line[0:-2] == "Language: en":
                pass
            else:
                f.write(line[0:-1]+" ")


def subtitle2txt_full_files(path):

    for (dirpath, dirnames, filenames) in os.walk(path):
        if filenames != []:

            for filename in filenames:
                filenamelist = filename.split(".")
                if filenamelist[-1] == str_name_subtitle:
                    f = open(path+filename, 'r', encoding='UTF-8')
                    linelist = f.readlines()

                    # print(linelist)
                    f2 = open(path+filenamelist[0]+".txt", "w")
                    counter = 1
                    for i in range(len(linelist)):
                        if (i+1) % 4 == 3:
                            #print("i", linelist[i][-2])
                            line_check_if_full_sentence(
                                linelist[i], pos4end, f2)


subtitle2txt_full_files(path)
