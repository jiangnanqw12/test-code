f = open("re.txt", "r")
f2 = open("re_p.txt", "w")
f3 = open("ty.txt", "r")
linelist = f.readlines()
linelist_ty = f3.readlines()
word_set = set()
for line in linelist:
    if line != "\n":
        wordlist = line[12:-1].split(" ")
        for word in wordlist:
            word = word.lower()
            # print(word)
            if word not in [" ", "-", "\n", '']:
                # print(word)
                if word[-1] in [",", ":", "!", "?", "\n", ")"]:
                    print(word)
                    word = word[0:-1]
                    print(word)
                if word[0] in [",", ":", "!", "?", "\n", "("]:
                    word = word[1:]

                if word[-1] == "\n":
                    print(word)
                    pass

                if word + "\n" not in linelist_ty:
                    # print(word)
                    # pass
                    # if word in linelist_ty:
                    # print(word)

                    word_set.add(word)
# print(word_set)
# for word in word_set:
#     f2.write(word+"\n")
