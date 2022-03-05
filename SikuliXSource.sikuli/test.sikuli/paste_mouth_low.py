
rePath="C:/data_Sikulixide/re.txt"
file_re=open(rePath)
lines_re=file_re.readlines()
q1=78
def paste_mouth_low():
    for i in range(len(lines_re)):
        #mouth
        linelist=lines_re[i].split(" ")
        click(Region(301,153+i*q1,9,13))#click rili
        click(Region(327,191+i*q1,15,16))#input
        if linelist[0]==4:
            paste(linelist[0][0])
            paste(linelist[0][1])
        elif linelist[0]==3:
            paste(linelist[0][0])
        click(Region(430,377+i*q1,23,12))#confirm click
paste_mouth_low()


