

f = open("re.txt", "r")
f2 = open("re_p.txt", "w")
f3 = open("ty.txt", "r")
linelist = f.readlines()
linelist_ty = f3.readlines()
word_set = set()
for line in linelist:

    if line != "\n" and line != []:
        wordlist = line[12:-1].split(" ")
        for word in wordlist:
            word = word.lower()
            # print(word)
            if word not in [" ", "-", "\n", '']:
                while(word != "" and (word[-1] in [",", ":", "!", "?", "\n", ")", "\r", ".", "]", " "])):
                    word = word[0:-1]
                    # print(word)
                while(word != "" and (word[0] in [",", ":", "!", "?", "\n", "(", "["])):
                    word = word[1:]
                    # print(word)
                # print(word, len(word))
                # for linetr in linelist_ty:
                #     print(linetr, len(linetr))
                if word+"\r"+"\n" not in linelist_ty:

                    pass
                    # if word in linelist_ty:
                    if (len(word) > 3):
                        print(word)

                        word_set.add(word)
                else:
                    pass
                    # print(word, len(word))

# print(word_set)
for word in word_set:
    f2.write(word+"\n")
