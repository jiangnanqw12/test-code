#hour
rePath="C:/data_Sikulixide/re.txt"
file_re=open(rePath)
lines_re=file_re.readlines()

#for i in range(len(lines_re)):
i=0
linelist=lines_re[i].split(" ")
click(Region(428,167+i*q1,14,14))#click shi zhong
click(Region(602,187+i*q1,27,16))#num
for j in range(3):
    click(Region(619,562+i*q1,7,13))#xiala
#click(Region(606,546+i*q1,12,15))#22

if len(linelist[1])==4:
    #string_hour=linelist[1][0]+linelist[1][1]
    #num_hour=eval(string_hour)
    #if num_hour==23:
    if linelist[1][0]==b"2":
        #click(Region(601,580+i*q1,8,12))#23
        click(Region(Region(602,575+i*q1,5,4)))#23
    else:
        click(Region(606,551+i*q1,11,10))#22
        print(22)
#click(Region(550,212+i*q1,25,13))#3