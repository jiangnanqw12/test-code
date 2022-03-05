rePath="C:/data_Sikulixide/re.txt"
file_re=open(rePath)
lines_re=file_re.readlines()
rePath="C:/data_Sikulixide/work.txt"
file_work=open(rePath)
lines_work=file_work.readlines()
q1=78
for i in range(len(lines_re)):
    linelist=lines_re[i].split(" ")
    #print(linelist[3])
    print(len(linelist[3]))
    print(linelist[3][1])
    if len(linelist[3])==4:
        #print(2)
        #string_hour=linelist[1][0]+linelist[1][1]
        #num_hour=eval(string_hour)
        if linelist[3][1]=="3" and linelist[3][0]=="2":
            print(1)
