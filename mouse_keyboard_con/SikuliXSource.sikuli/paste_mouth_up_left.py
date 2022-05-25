def day2pos(pos0000,day_string,day_one_offset):
    a=29
    b=20
    #posZ=[kc,jd] z/7=j..k
    #z->[xa,yb] z/6=y...x
    end=[]
    day=eval(day_string)
    print(day)
    #string_num=linelist[1][2]+linelist[1][3]
    num=day+day_one_offset
    #print(num)
    j=num//7
    k=num%7
    end=[pos0000[0]+k*a,pos0000[1]+j*b]
    return end
def paste_mouth_up_left():

    for i in range(len(lines_re)):
        #mouth
        linelist=lines_re[i].split(" ")

        click(Region(261,164+i*q1,15,15))#click rili
        wait(0.1)
        click(Region(290,204+i*q1,25,16))#input mon
        mon_string_num=linelist[0][0]+linelist[0][1]
        pos0000_mon=[283,230]

        mon_num_pos=mon2pos(pos0000_mon,mon_string_num)
        click(Region(mon_num_pos[0],mon_num_pos[1]+i*q1,25,13))

        wait(0.1)
        day_string=linelist[0][2]+linelist[0][3]

        pos0000=[245,251]
        if mon_string_num=='01':
            day_one_offset=2
        if mon_string_num=='10':
            day_one_offset=3
        elif mon_string_num=='11':
            day_one_offset=-1
        try:
            end=day2pos(pos0000,day_string,day_one_offset)
            click(Region(end[0],end[1]+i*q1,25,13))
            wait(0.1)
        except:
            click(Region(Region(33,178,39,50)))
            print(1)
        #click(Region(398,391+i*q1,20,18))#confirm click
paste_mouth_up_left()