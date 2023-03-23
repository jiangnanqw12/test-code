string_name='姜楠'
string_name.encode("utf-8")
q1=78

def paste_name_low():

    for i in range(6):
        wait(0.5)
        click(Region(1626,152+i*q1,44,17))
        wait(0.5)
        paste(unicode(string_name,encoding="utf-8"))
        wait(0.5)
        click(Region(1624,179+i*q1,32,10))

paste_name_low()