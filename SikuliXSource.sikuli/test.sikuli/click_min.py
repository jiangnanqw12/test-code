#coding=utf-8
a=33
b=19
#z->[xa,yb] z/6=y...x
start_pos=[481,188]

#110%\
rePath="C:/data_Sikulixide/re.txt"
file_re=open(rePath)
lines_re=file_re.readlines()
rePath="C:/data_Sikulixide/work.txt"
file_work=open(rePath)
lines_work=file_work.readlines()
q1=78

def get_min_pos(string_num,start_pos):
    a=33
    b=19
    #z->[xa,yb] z/6=y...x
    end=[]
    #string_num=linelist[1][2]+linelist[1][3]
    num=eval(string_num)
    y=num//6
    x=num%6
    end=[x*a,y*b]
    return end

def click_clock_down_left():
    for i in range(len(lines_re)):
        click(Region(444,139+i*q1,14,14))#click shi zhong
        click(Region(626,161+i*q1,27,16))#num
        linelist=lines_re[i].split(" ")
        for j in range(3):
            click(Region(643,541+i*q1,7,13))#xiala
        #click(Region(606,546+i*q1,12,15))#22
        if len(linelist[1])==4:
            #string_hour=linelist[1][0]+linelist[1][1]
            #num_hour=eval(string_hour)
            if linelist[1][1]=="3" and linelist[1][0]=="2":
                click(Region(Region(621,541+i*q1,5,4)))#23

            elif linelist[1][1]=="2" and linelist[1][0]=="2":
                click(Region(619,524+i*q1,11,10))#22
            elif linelist[1][0]=="0":
                click(Region(646,217+i*q1,11,10))#shang la
                click(Region(621,185+i*q1,11,10))#0 dian
            #get_min_pos
            string_num=linelist[1][2]+linelist[1][3]
            # num=eval(string_num)
            # y=num//6
            # x=num%6
            # end=[x*a,y*b]
            end=get_min_pos(string_num,start_pos)
            click(Region(end[0]+start_pos[0],end[1]+start_pos[1]+i*q1,25,13))#3
click_clock_down_left()

