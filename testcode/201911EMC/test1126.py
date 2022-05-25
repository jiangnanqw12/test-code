#dark current
import numpy as np
import matplotlib.pyplot as plt





def import_data_dark():
    for mode in range(3):
        test_data_dark=[]
        for time in inttimes:
            data=[]
            for i in range(3):
                mat=np.loadtxt(dir1+str(mode)+"_"+str(time)+"_"+str(i)+dir2)
                data.append(mat)
            test_data_dark.append(data)
        dark_data[mode]=test_data_dark



def get_mean():
    for key in dark_data:
        meanx={}
        for t in range(len(inttimes)):
            s=np.zeros((512,512))
            
            for i in range(3):
                s+=(dark_data[key])[t][i]
                sr=str(mode)+str(inttimes[t])
            meanx[inttimes[t]]=s/3
        mean[key]=meanx
    
        # filename="mean"+str(mode+n1)+".txt"
        # print(mean[mode+n1])
        # print("mode",mode+n1,"\n",mean[mode+n1])
        # np.savetxt(filename,list(mean[mode+n1]),fmt="%.2f")



def get_mean_mean():
    for keymode in mean:
        data={}
        for keytime in mean[keymode]:
            s=np.sum(mean[keymode][keytime])
            data[keytime]=s/512/512
        mean_mean[keymode]=data

def get_a_b(keymode):
    keymode
    x=np.array(inttimes)/1000000
    x_=np.mean(x)
    for time in inttimes:
        y.append(mean_mean[keymode][time])
        print("y",mean_mean[keymode][time])
    y_=np.mean(y)
    print("y_",y_)
    a1=0
    a2=0
    for i in range(len(x)):
        a1+=(x[i]-x_)*(y[i]-y_)
        a2+=(x[i]-x_)**2
    print("a1",a1)
    print("a2",a2)
    a=a1/a2
    print("a",a)
    b=y_-a*x_
    #print(b)
    
    return a,b,x,y

#m>=3 p>=5
test_data=[]
#test_data_dark=[]
inttime=500000#ns
inttimes=range(100000,700000,100000)#1s=1000000us 
#[0, 200000, 400000, 600000, 800000]
mode=0
i=0
dir1="IS_Data7/Matrix_512x512_Line"
dir2=".txt"
dark_data={}
mean={}
mean_mean={}
n1=26
n2=28
xa=[]
ya=[]
x_=0
y_=0
a=[]
b=[]
import_data_dark()
get_mean()
get_mean_mean()
for mode in range(3):
    ax,bx,x,y=get_a_b(mode)
    a.append(ax)
    b.append(bx)
    xa.append(x)
    ya.append(y)
print("a:",a," b:",b)
#plt.plot(xa[0],ya[0])
#plt.scatter(xa[0],ya[0])

