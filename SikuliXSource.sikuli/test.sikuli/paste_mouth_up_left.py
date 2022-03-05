rePath="C:/data_Sikulixide/re.txt"
file_re=open(rePath)
lines_re=file_re.readlines()
def mon2pos(pos0000_mon,mon_string_num):
    mon_offset=-1
    a=31
    b=23
    #z/6=j....k
    #z->[j*a,k*b]
    mon=eval(mon_string_num)
    print(mon)
    num=mon+mon_offset
    j=num//6
    k=num%6
    end=[pos0000_mon[0]+j*a,pos0000_mon[1]+k*b]
    return end

def day2pos(pos0000,day_string,day_one_offset):
    a=29
    b=19
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

        end=day2pos(pos0000,day_string,day_one_offset)
        click(Region(end[0],end[1]+i*q1,25,13))
        wait(0.1)
def main():
    paste_mouth_up_left()

if __name__=='__main__':
    main()



