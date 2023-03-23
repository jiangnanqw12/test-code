
SeedPath="C:/data_Sikulixide/re.txt"
file=open(SeedPath)
q1=78
#linelist=file.readli
#for line in file.xreadlines():
def paste_fee():
    lines=file.readlines()
    #for line in lines:
    for i in range(len(lines)):
        linelist=lines[i].split(" ")
        wait(1)
        click(Region(1426,542+i*q1,43,23))#fp1 fee
        wait(1)
        paste(linelist[-1])
