rePath="C:/data_Sikulixide/re.txt"
file_re=open(rePath)
lines_re=file_re.readlines()
def paste_mouth_up_left2():
    #mouth
    for i in range(len(lines_re)):
        linelist=lines_re[i].split(" ")
        click(Region(267,167+i*q1,15,15))#click rili
        click(Region(290,204+i*q1,25,16))#
        if linelist[0]==4:
            paste(linelist[0][0])
            paste(linelist[0][1])
        elif linelist[0]==3:
            paste(linelist[0][0])
        click(Region(398,391+i*q1,20,18))#confirm click
paste_mouth_up_left2()