f = open("re.txt", "r")
f2 = open("re_p.txt", "w")
f3 = open("ty.txt", "r")
linelist = f.readlines()
linelist_ty = f3.readlines()
# for wordty in linelist_ty:
#     if wordty[0:] == "of\n":
#         print(wordty)
# print(int("a"))
word_set = set()
for line in linelist:
    if line != "\n":
        # print(bytes(line, 'utf-8'))
        # print(bytes(line))
        # print(line)
        if (line[0:7] == "Concept"):
            # print(line)
            # f2.write(line[12:-1])
            # f2.write("\n")
            wordlist = line[12:-1].split(" ")
            for word in wordlist:
                # print(word)
                if word[-1] in [",", ":", "!", "?"]:
                    # print(word)
                    word = word[0:-1]
                    # print(word)
                if word[-1] == "\n":
                    print(word)
                    pass
                if word + "\n" not in linelist_ty:
                    # print(word)
                    # pass
                    # if word in linelist_ty:
                    #     print(word)
                    word_set.update(word)

        elif (line[0:6] == "Lesson"):
            # print(line)
            # f2.write(line[11:-1])
            # f2.write("\n")
            pass
        elif(line[0:6] == "Module"):
            # print(line)
            pass
        # elif (line[0:7] == "Project"):
        else:
            # f2.write(line)
            pass
