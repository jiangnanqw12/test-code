rePath="C:/data_Sikulixide/re.txt"
file_re=open(rePath)
lines_re=file_re.readlines()
rePath="C:/data_Sikulixide/work.txt"
file_work=open(rePath)
lines_work=file_work.readlines()
q1=78
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
        end=min2pos(min_string,pos0000_min)
        click(Region(end[0],end[1]+i*q1,25,13))#min

click_clock_down_right()