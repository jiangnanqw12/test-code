import os
from pdfProcess import list_reform
from pdfProcess import testclip


def zhihmulu2txt(path):
    f = open(path+"re.zhi2txt1", encoding="utf-8")
    f2 = open(path+"re.zhi2txt2", "w", encoding="utf-8")
    linelist = f.readlines()
    for line in linelist:
        if line[0] == "第":
            f2.write("# "+line+"\n")
            f2.write(line+"\n")
    f.close
    f2.close()


if __name__ == '__main__':
    path = os.getcwd()+"/"
    testclip.copy_text_from_clip(path, "zhi2txt1")
    zhihmulu2txt(path)
