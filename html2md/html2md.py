import aspose.words as aw

# -*- coding: utf-8*-
import os

path = os.getcwd()+"/"


def html2md(path):

    listfiles = os.listdir(path)

    # print(listfiles)
    for i in range(len(listfiles)):
        filename = listfiles[i]  # get all file list
        filenamelist = filename.split(sep=".")
        if filenamelist[-1] == "html":

            doc = aw.Document(path+filename)
            doc.save("md1/"+filenamelist[0]+filenamelist[1]+".md")

# 后面加入换行符


def formatMD(path):
    listfiles = os.listdir(path+"/md1/")

    # print(listfiles)
    for i in range(len(listfiles)):
        filename = listfiles[i]  # get all file list
        filenamelist = filename.split(sep=".")
        if filenamelist[-1] == "md":
            f = open(path+"/md1/"+filename, 'r', encoding='UTF-8')
            f2 = open(path+"/md1/"+"Concept "+filename, "w", encoding='UTF-8')
            linelist = f.readlines()
            for j in range(len(linelist)):
                if j == 0:
                    continue
                # print(linelist[j])
                # print(linelist[j].find(
                #     "Evaluation Only. Created with Aspose.Words. Copyright 2003-2022 Aspose Pty Ltd."))
                flag = 0

                for str2 in skiplist:

                    if ((linelist[j].find(str2)) != -1):
                        flag += 1
                if ((linelist[j].find("- ")) != -1) and ((linelist[j].find(".html")) != -1):
                    flag += 1
                if flag == 0:
                    f2.write(linelist[j]+"\n")

            f.close()
            f2.close()


if __name__ == '__main__':
    path = os.getcwd()+"/"
    html2md(path)

    skiplist = [
        "Evaluation Only. Created with Aspose.Words. Copyright 2003-2022 Aspose Pty Ltd.",
        "udacimak",
        "Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit",
        "[Back to Home]", "[02. Welcome from Sebastian]",
        "- [01. The Magic of Self-Driving Cars](/mnt/c/Users/shadow/Documents/Part 01-Module 01-Lesson 01_Introduction/01. The Magic of Self-Driving Cars.html)",
        "- [02. Welcome from Sebastian](/mnt/c/Users/shadow/Documents/Part 01-Module 01-Lesson 01_Introduction/02. Welcome from Sebastian.html)",
        "- [03. Meet the Team](/mnt/c/Users/shadow/Documents/Part 01-Module 01-Lesson 01_Introduction/03. Meet the Team.html)",
        "- [04. Student Services](/mnt/c/Users/shadow/Documents/Part 01-Module 01-Lesson 01_Introduction/04. Student Services.html)",
        "- [05. Community Code of Conduct](/mnt/c/Users/shadow/Documents/Part 01-Module 01-Lesson 01_Introduction/05. Community Code of Conduct.html)",
        "- [06. Deadline Policy](/mnt/c/Users/shadow/Documents/Part 01-Module 01-Lesson 01_Introduction/06. Deadline Policy.html)",
        "- [07. First Two Weeks Learning Plan](/mnt/c/Users/shadow/Documents/Part 01-Module 01-Lesson 01_Introduction/07. First Two Weeks Learning Plan.html)",
        "- [08. Class Schedule](/mnt/c/Users/shadow/Documents/Part 01-Module 01-Lesson 01_Introduction/08. Class Schedule.html)",
        "- [09. Expectations for this Nanodegree](/mnt/c/Users/shadow/Documents/Part 01-Module 01-Lesson 01_Introduction/09. Expectations for this Nanodegree.html)",
        "- [Back to Home](/mnt/c/Users/shadow/Documents/Part 01-Module 01-Lesson 01_Introduction/../index.html)",
        "- [10. Readiness Introduction](/mnt/c/Users/shadow/Documents/Part 01-Module 01-Lesson 01_Introduction/10. Readiness Introduction.html)"]
    formatMD(path)
