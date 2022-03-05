rePath="C:/data_Sikulixide/work.txt"
file_work=open(rePath)
lines_work=file_work.readlines()
def paste_work_low():
    for i in range(6):
        wait(0.5)
        click(Region(1341,136+i*q1,62,45))
        for line in lines_work:
            wait(0.5)
            #paste(line)
            line.encode("utf-8")
            paste(unicode(line,encoding="utf-8"))
paste_work_low()