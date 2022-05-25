rePath="C:/data_Sikulixide/work.txt"
file_work=open(rePath)
lines_work=file_work.readlines()
def paste_work():
    for i in range(6):
        wait(1)
        click(Region(1204,533+i*q1,79,36))
        for line in lines_work:
            wait(1)
            #paste(line)
            line.encode("utf-8")
            paste(unicode(line,encoding="utf-8"))
paste_work()