# from base64 import encode
# from msilib.schema import Binary
import os
# -*- coding: UTF-8 -*-
# path = "/mnt/d/00mooc/Sensor Fusion v1.0.0/Part 04-Module 01-Lesson 01_Introduction/"
# filename = "02 ND313 C03 L01 A01 Course Intro-1Ainh-JHmGwen.txt"


def reformat_txt_full_sentence(path, filename, pos4end):
    f = open(path+filename)

    f2 = open(path+"uda"+filename+str(pos4end), "w")
    linelist = f.readlines()
    for line in linelist:
        if line != []:
            # print((line[-2])=="\n")
            # print(line[-2])
            try:
                line[-pos4end]
            except:
                print(line)
            if line[-pos4end] == ".":

                f2.write(line)
                f2.write("\n")
            else:
                if line[0:-1] == "Language: en":
                    pass
                else:
                    f2.write(line[0:-2]+" ")
    f.close
    f2.close()


# listfiles = os.listdir()
# print(listfiles)
f = []
#mypath = "/mnt/d/00mooc/Sensor Fusion v1.0.0/Part 04-Module 01-Lesson 01_Introduction/"
mypath = os.getcwd()
for (dirpath, dirnames, filenames) in os.walk(mypath):
    # print(dirpath)
    # print(dirnames)
    # print(filenames)

    if filenames != []:

        for filename in filenames:
            filenamelist = filename.split(".")
            if filenamelist[-1] == "txt":
                reformat_txt_full_sentence(dirpath+"/", filename, 2)
