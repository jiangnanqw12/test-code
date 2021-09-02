import os
path = "D:\\BaiduNetdiskDownload\\00mooc\\csapp\\csapp_lectures\\lectures"
listfiles = os.listdir(path)
f = open("csapp.txt", "w")
f3 = open("ty.txt", "r")
linelist_ty = f3.readlines()
word_set = set()


def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        for i in s:
            unicodedata.numeric(i)  # 把一个表示数字的字符串转换为浮点数返回的函数
            # return True
        return True
    except (TypeError, ValueError):
        pass
    return False


for filename in listfiles:
    # print(filename)
    fl = filename.split(".")
    if fl[-1] == "pdf":
        # print(fl[0])
        fnl2 = fl[0].split("-")
        # print(fnl2)
        for word in fnl2:
            if not is_number(word):
                if word + "\n" not in linelist_ty:
                    if is_number(word[-1]):
                        word = word[0:-1]
                        # print(word)
                    word_set.add(word)
for word in word_set:
    f.write(word)
    f.write("\n")
