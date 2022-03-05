#import sys
#coding=utf-8

def get_min_pos(string_num,start_pos):
    a=32
    b=19
    #z->[xa,yb] z/6=y...x
    end=[]
    #string_num=linelist[1][2]+linelist[1][3]
    num=eval(string_num)
    y=num//6
    x=num%6
    end=[x*a,y*b]
    return end
def fill_start_point():
    # qidian
    for i in range(6):
        wait(0.2)
        click(Region(581,545+i*q1,71,20))#fp start point
        wait(0.2)
        paste(unicode(string_start,encoding="utf-8"))
def fill_des():
    for i in range(6):
        wait(0.2)
        click(Region(1025,543+i*q1,66,26))#fp1 zhongdian
        wait(0.2)
        paste(unicode(string_des,encoding="utf-8"))
def paste_fee():
    #for line in lines:
    for i in range(len(lines_re)):
        linelist=lines_re[i].split(" ")
        wait(0.1)
        click(Region(1426,542+i*q1,43,23))#fp1 fee
        wait(0.1)
        paste(linelist[2])

def paste_work_up():
    for i in range(6):
        wait(0.1)
        click(Region(1204,533+i*q1,79,36))
        for line in lines_work:
            wait(0.1)
            #paste(line)
            line.encode("utf-8")
            paste(unicode(line,encoding="utf-8"))
def init_paste():
    click(Region(1304,573,99,35))#click baoxiao
    wait(3)
    click(Region(422,385,118,27))#fapiao xingshi
    wait(0.1)
    click(Region(440,460,91,15))#quan zhizhi fapiao
    wait(0.1)
    click(Region(1247,353,90,20))#baoxiao dan fenlei
    wait(0.1)
    click(Region(1247,385,63,17))#shinei jiaotong fapiao
    wait(0.1)
    click(Region(1242,384,110,20))#fapiao shuliang
    wait(0.1)
    paste('6')
    wait(0.1)
    click(Region(419,420,35,19))#shifou jiekuan
    wait(0.1)
    click(Region(429,460,11,13))#fou
    for i in range(6):
        wait(0.1)
        click(Region(1698,445,28,28))#++


#reconstruct input
def reconstruct_date_input():
    click(Region(1905,882,13,22))#xia la
    for i in range(3):
        click(Region(1903,125,13,11))#shang la 3  ci

def mon2pos(pos0000_mon,mon_string_num):
    mon_offset=-1
    a=31
    b=23
    #z/6=j....k
    #z->[j*a,k*b]
    mon=eval(mon_string_num)
    #print(mon)
    num=mon+mon_offset
    j=num//6
    k=num%6
    end=[pos0000_mon[0]+j*a,pos0000_mon[1]+k*b]
    return end

def day2pos(pos0000,day_string,day_one_offset):
    a=29
    b=20
    #posZ=[kc,jd] z/7=j..k
    #z->[xa,yb] z/6=y...x
    end=[]
    day=eval(day_string)
    #string_num=linelist[1][2]+linelist[1][3]
    num=day+day_one_offset
    j=num//7
    k=num%7
    end=[pos0000[0]+k*a,pos0000[1]+j*b]
    return end
def paste_mouth_up_left():

    for i in range(len(lines_re)):
        #mouth
        linelist=lines_re[i].split(" ")
        click(Region(267,171+i*q1,15,15))#click rili
        wait(0.1)
        click(Region(290,204+i*q1,25,16))#input mon
        mon_string_num=linelist[0][0]+linelist[0][1]
        pos0000_mon=[283,230]

        mon_num_pos=mon2pos(pos0000_mon,mon_string_num)
        click(Region(mon_num_pos[0],mon_num_pos[1]+i*q1,25,13))

        wait(0.1)
        day_string=linelist[0][2]+linelist[0][3]

        pos0000=[250,257]
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
            print(1)
        #click(Region(398,391+i*q1,20,18))#confirm click

def paste_mouth_up_right():
    for i in range(len(lines_re)):
        #mouth
        linelist=lines_re[i].split(" ")
        click(Region(722,171+i*q1,15,15))#click rili
        wait(0.1)
        click(Region(754,210+i*q1,25,16))#input mon
        mon_string_num=linelist[0][0]+linelist[0][1]
        pos0000_mon=[740,229]

        mon_num_pos=mon2pos(pos0000_mon,mon_string_num)
        click(Region(mon_num_pos[0],mon_num_pos[1]+i*q1,25,13))
        #day
        wait(0.1)
        day_string=linelist[0][2]+linelist[0][3]

        pos0000=[706,257]
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
            pass

def min2pos(min_string,pos0000_min):
    a=32
    b=19
    #z->[xa,yb] z/6=y...x
    end=[]
    #string_num=linelist[1][2]+linelist[1][3]
    num=eval(min_string)
    y=num//6
    x=num%6
    end=[pos0000_min[0]+x*a,pos0000_min[1]+y*b]
    return end
def click_clock_up_left():
    for i in range(len(lines_re)):
        click(Region(428,167+i*q1,14,14))#click shi zhong
        click(Region(602,187+i*q1,27,16))#num
        linelist=lines_re[i].split(" ")
        for j in range(3):
            click(Region(619,562+i*q1,7,13))#xiala
        #click(Region(606,546+i*q1,12,15))#22
        if len(linelist[1])==4:
            #string_hour=linelist[1][0]+linelist[1][1]
            #num_hour=eval(string_hour)
            if linelist[1][0]=="2":
                if linelist[1][1]=="3":
                    click(Region(602,575+i*q1,5,4))#23

                elif linelist[1][1]=="2":
                    click(Region(606,551+i*q1,11,10))#22
            elif linelist[1][0]=="0":
                click(Region(630,238+i*q1,11,10))#shang la
                click(Region(609,213+i*q1,11,10))#0 dian

        min_string=linelist[1][2]+linelist[1][3]
        pos0000_min=[469,220]

        try:
            end=min2pos(min_string,pos0000_min)
            click(Region(end[0],end[1]+i*q1,25,13))#min
        except:
            print(1)

def click_clock_up_right():
    for i in range(len(lines_re)):
        click(Region(887,170+i*q1,14,14))#click shi zhong
        click(Region(1067,191+i*q1,27,16))#num
        linelist=lines_re[i].split(" ")
        for j in range(3):
            click(Region(1086,578+i*q1,7,13))#xiala

        if linelist[3][0]=="2":
            if linelist[3][1]=="3":
                click(Region(Region(1061,577+i*q1,5,4)))#23
            elif linelist[3][1]=="2":
                click(Region(1058,558+i*q1,11,10))#22
        elif linelist[3][0]=="0":
            click(Region(1081,241+i*q1,11,10))#shang la
            click(Region(1062,214+i*q1,11,10))#0 dian

        min_string=linelist[3][2]+linelist[3][3]
        pos0000_min=[917,214]
        try:
            end=min2pos(min_string,pos0000_min)
            click(Region(end[0],end[1]+i*q1,25,13))#min
        except:
            pass

def reconstruct_sec():
    for i in range(6):
        wait(0.5)
        click(Region(1700,644,21,21))
    click(Region(1903,868,14,18))



def click_clock_down_left():
    for i in range(len(lines_re)):
        click(Region(447,160+i*q1,14,14))#click shi zhong
        click(Region(626,161+i*q1,27,16))#num
        linelist=lines_re[i].split(" ")
        for j in range(3):
            click(Region(643,541+i*q1,7,13))#xiala
        #click(Region(606,546+i*q1,12,15))#22
        if len(linelist[1])==4:
            if linelist[1][0]=="2":
                if linelist[1][1]=="3":
                    click(Region(624,561+i*q1,5,4))#23
                elif linelist[1][1]=="2":
                    click(Region(625,541+i*q1,11,10))#22
            elif linelist[1][0]=="0":
                click(Region(646,217+i*q1,11,10))#shang la
                click(Region(626,198+i*q1,11,10))#0 dian
        min_string=linelist[1][2]+linelist[1][3]
        pos0000_min=[483,207]
        try:
            end=min2pos(min_string,pos0000_min)
            click(Region(end[0],end[1]+i*q1,25,13))#min
        except:
            print(1)

def click_clock_down_right():
    for i in range(len(lines_re)):
        click(Region(722,159+i*q1,14,14))#click shi zhong
        click(Region(904,178+i*q1,27,16))#num
        linelist=lines_re[i].split(" ")
        for j in range(3):
            click(Region(920,559+i*q1,7,13))#xiala

        if linelist[3][0]=="2":
            if linelist[3][1]=="3":
                click(Region(Region(899,561+i*q1,5,4)))#23
            elif linelist[3][1]=="2":
                click(Region(897,541+i*q1,11,10))#22
        elif linelist[3][0]=="0":
            click(Region(919,232+i*q1,11,10))#shang la
            click(Region(898,198+i*q1,11,10))#0 dian

        min_string=linelist[3][2]+linelist[3][3]
        pos0000_min=[756,204]
        try:
            end=min2pos(min_string,pos0000_min)
            click(Region(end[0],end[1]+i*q1,25,13))#min
        except:
            print(1)


def paste_mouth_down_right():
    for i in range(len(lines_re)):
    #mouth
        linelist=lines_re[i].split(" ")
        click(Region(571,152+i*q1,15,15))#click rili
        wait(0.1)
        click(Region(599,191+i*q1,25,16))#input mon
        mon_string_num=linelist[0][0]+linelist[0][1]
        pos0000_mon=[589,212]

        mon_num_pos=mon2pos(pos0000_mon,mon_string_num)
        click(Region(mon_num_pos[0],mon_num_pos[1]+i*q1,25,13))
        #day
        wait(0.1)
        day_string=linelist[0][2]+linelist[0][3]

        pos0000=[558,241]
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
            pass

def paste_mouth_down_left():
    for i in range(len(lines_re)):
    #mouth
        linelist=lines_re[i].split(" ")
        click(Region(301,157+i*q1,15,15))#click rili
        wait(0.1)
        click(Region(328,191+i*q1,25,16))#input mon
        mon_string_num=linelist[0][0]+linelist[0][1]
        pos0000_mon=[318,212]

        mon_num_pos=mon2pos(pos0000_mon,mon_string_num)
        click(Region(mon_num_pos[0],mon_num_pos[1]+i*q1,25,13))
        #day
        wait(0.1)
        day_string=linelist[0][2]+linelist[0][3]

        pos0000=[284,242]
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
            pass
def paste_des_start_low():
    # qidian
    for i in range(6):
        wait(0.1)
        click(Region(814,137+i*q1,68,43))#fp start point
        wait(0.1)
        paste(unicode(string_start,encoding="utf-8"))
        wait(0.1)
        paste("\n")
        #wait(1)
        wait(0.1)
        paste(unicode(string_des,encoding="utf-8"))

def paste_fee_low():
    #for line in lines:
    for i in range(len(lines_re)):
        linelist=lines_re[i].split(" ")
        wait(0.1)
        click(Region(1018,148+i*q1,47,20))#fee low
        wait(0.1)
        paste(linelist[2])


def paste_taxi():
    #for line in lines:
    for i in range(6):
        wait(0.1)
        click(Region(1176,143+i*q1,89,40))#
        #wait(0.5)
        wait(0.1)
        string_taxi="出租车"
        string_taxi.encode("utf-8")
        paste(unicode(string_taxi,encoding="utf-8"))

def paste_num_fapiao_low():
    for i in range(6):
        wait(0.1)
        click(Region(1522,152+i*q1,32,15))
        wait(0.1)
        paste("1")

def paste_work_low():
    for i in range(6):
        wait(0.1)
        click(Region(1341,136+i*q1,62,45))
        for line in lines_work:
            wait(0.1)
            #paste(line)
            line.encode("utf-8")
            paste(unicode(line,encoding="utf-8"))

def paste_name_low():

    for i in range(6):
        wait(0.1)
        click(Region(1626,152+i*q1,44,17))
        wait(0.1)
        paste(unicode(string_name,encoding="utf-8"))
        wait(0.1)
        click(Region(1624,179+i*q1,32,10))

def save_and_exit():
    #click()#上拉
    click(Region(1831,93,23,14))#保存
    wait(1)
    click(Region(1888,12,23,14))#exit()
def main():
    print('in: ')
    for line in lines_re:
        print(line)
    init_paste()
    #qidian
    fill_start_point()
    #zhongdian
    fill_des()


    paste_fee()

    paste_work_up()
    reconstruct_date_input()
    paste_mouth_up_left()
    paste_mouth_up_right()
    click_clock_up_left()
    click_clock_up_right()
    reconstruct_sec()
    click_clock_down_left()
    click_clock_down_right()
    paste_mouth_down_left()
    paste_mouth_down_right()
    paste_des_start_low()
    paste_fee_low()
    paste_taxi()
    paste_num_fapiao_low()

    paste_work_low()
    paste_name_low()
    save_and_exit()
if __name__ == "__main__":
    wait(1)
    string_start='上微总部'
    string_start.encode("utf-8")
    string_des="庭安路兰嵩路"
    string_des.encode("utf-8")
    #110%
    q1=78
    workPath="C:/data_Sikulixide/work.txt"
    file_work=open(workPath)
    lines_work=file_work.readlines()
    string_name='姜楠'
    string_name.encode("utf-8")
    file_re_t=open("C:/data_Sikulixide/re_t.txt")
    lines_re_t=file_re_t.readlines()
    #rePath="C:/data_Sikulixide/re.txt"
    #file_re=open(rePath,'w+')
    lines_re=[]
    for i in range(len(lines_re_t)):
        #file_re.write(lines_re_t[i])
        lines_re.append(lines_re_t[i])
        i+=1
        if i%6==0:
            #file_re.close()
            print(i)
            #lines_re=file_re.readlines()
            print('out: ')
            for line in lines_re:
                print(line)
            main()
            lines_re=[]
            #file_re=open(rePath,'w+')



