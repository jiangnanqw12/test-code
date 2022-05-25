rePath="C:/data_Sikulixide/re.txt"
file_re=open(rePath)
lines_re=file_re.readlines()

i=0
linelist=lines_re[i].split(" ")
if linelist[1][0]=="2":
    print(1)