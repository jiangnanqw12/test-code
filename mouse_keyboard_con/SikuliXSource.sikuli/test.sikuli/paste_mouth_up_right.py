rePath="C:/data_Sikulixide/re.txt"
file_re=open(rePath)
lines_re=file_re.readlines()
def get_mon_num_pos(mon_start_pos,mon_string_num):
    e=31
    f=23
    #z/7=j....k
    #z->[j*e,f*k]
    mon_num=eval(mon_string_num)
    j=mon_num//7
    k=mon_num%7
    end=[j*e,f*k]
    return end

def get_day_num_pos(start_pos,num_day,one_number):
    c=32
    d=19
    #posZ=[kc,jd] z/7=j..k
    #z->[xa,yb] z/6=y...x
    end=[]
    #string_num=linelist[1][2]+linelist[1][3]
    num=num_day+one_number-1
    j=num//8
    k=num%8
    end=[k*c,j*d]
    return end
def paste_mouth_up_right():
    for i in range(len(lines_re)):
        #mouth
        linelist=lines_re[i].split(" ")
        click(Region(721,161+i*q1,15,15))#click rili
        wait(0.1)
        click(Region(757,204+i*q1,25,16))#
        mon_string_num=linelist[0][0]+linelist[0][1]
        print(mon_string_num)
        mon_start_pos=[749,224]
        mon_num_pos=get_mon_num_pos(mon_start_pos,mon_string_num)
        click(Region(mon_num_pos[0]+mon_start_pos[0],mon_num_pos[1]+mon_start_pos[1]+i*q1,25,13))
        wait(0.1)
        string_num=linelist[0][2]+linelist[0][3]
        start_pos=[710,254]
        one_number=4#start from 0
        num_day=eval(string_num)
        print(string_num)
        end=get_day_num_pos(start_pos,num_day,one_number)
        click(Region(end[0]+start_pos[0],end[1]+start_pos[1]+i*q1,25,13))
        wait(0.1)
        #click(Region(398,391+i*q1,20,18))#confirm click
paste_mouth_up_right()