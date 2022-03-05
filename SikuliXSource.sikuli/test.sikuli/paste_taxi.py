def paste_taxi():
    #for line in lines:
    for i in range(6):

        click(Region(1176,143+i*q1,89,40))#
        #wait(0.5)
        string_taxi="出租车"
        string_taxi.encode("utf-8")
        paste(unicode(string_taxi,encoding="utf-8"))
paste_taxi()