import os
#coding in utf-8

def text_replace(path):
    listdir = os.listdir(path)
    replace_list = [
        ["", " $$\sigma$ "],
    ["Ã¢Ë†Å¡2","$$\sqrt\{2\}$"],
    ["ˆx","$$\hat x$"],
    ["","$$\\alpha$"],
    ["","$$\\beta$"]
    ]
    #replace_list.append(["", " $$\sigma$ "])
    for i in range(len(listdir)):

        filename = listdir[i]
        filenamelist = filename.split(sep=".")
        if filenamelist[-1] == "pdftext2":

            f = open(path+filename, 'r', encoding='UTF-8')
            linelist = f.readlines()

            # print(linelist)
            f2 = open(path+filenamelist[0]+".pdftext3", "w", encoding='UTF-8')
            for i in range(len(linelist)):


                line=linelist[i]
                for j in range(len(replace_list)):
                    # idx = line.find(replace_list[j][0])
                    # idx2 = line.find("ˆx")
                    # print(idx2)
                    line = line.replace(
                        replace_list[j][0], replace_list[j][1])
                f2.write(line)

                # print(linelist[i][-1])
                # idx = line.find("")
                # print(idx)
                # if idx != -1:
                #     print(line)
                #     f2.write(line)
                #     f2.write("$$\sigma$$")
                #     line.replace("", "$$\sigma$$")
                #     print(line)
                #     f2.write(line)
                # f2.write(linelist[i])


if __name__ == '__main__':
    path = os.getcwd()+"/"
    text_replace(path)
