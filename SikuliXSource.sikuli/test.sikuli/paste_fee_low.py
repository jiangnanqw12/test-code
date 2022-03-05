rePath="C:/data_Sikulixide/re.txt"
file_re=open(rePath)
lines_re=file_re.readlines()
def paste_fee_low():
    #for line in lines:
    for i in range(len(lines)):
        linelist=lines_re[i].split(" ")
        wait(0.5)
        click(Region(1018,148+i*q1,47,20))#fee low
        wait(0.5)
        paste(linelist[-1])
paste_fee_low()