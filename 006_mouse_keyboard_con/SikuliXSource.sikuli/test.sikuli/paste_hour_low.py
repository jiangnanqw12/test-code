#hour
rePath="C:/data_Sikulixide/re.txt"
file_re=open(rePath)
lines_re=file_re.readlines()

for i in range(len(lines_re)):
    click(Region(441,151,13,15))#click shi zhong
    click(Region(619,172,17,11))#num
    linelist=lines_re[i].split(" ")
    for j in range(3):
        click(Region(651,553,11,9))#xiala
    #click(Region(606,546+i*q1,12,15))#22
    if len(linelist[1])==4:
        string_hour=linelist[1][0]+linelist[1][1]
        num_hour=eval(string_hour)
        if num_hour==23:
            #click(Region(601,580+i*q1,8,12))#23
            click()#23
        else:
            click()#22
            print(22)
    click()#3