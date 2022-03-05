string_start='上微总部'
string_start.encode("utf-8")
string_des="庭安路兰嵩路"
string_des.encode("utf-8")

q1=78

def paste_des_start_low():
    # qidian
    for i in range(6):
        #wait(1)
        click(Region(814,137+i*q1,68,43))#fp start point
        #wait(1)
        paste(unicode(string_start,encoding="utf-8"))
        paste("\n")
        #wait(1)
        paste(unicode(string_des,encoding="utf-8"))
paste_des_start_low()