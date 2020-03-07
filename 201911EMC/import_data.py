
import numpy as np






def import_data_dark():
    mode=0
    for time in inttimes:
        data=[]
        for i in range(10):
            mat=np.loadtxt(dir1+str(mode)+"_"+str(time)+"_"+str(i)+dir2)
            data.append(mat)
        test_data_dark.append(data)
def import_data(test_data,n1,n2):#n1 begin n2 end
    for mode in range(n1,n2+1):
        data=[]
        for i in range(10):
            mat=np.loadtxt(dir1+str(mode)+"_"+str(inttime)+"_"+str(i)+dir2)
            data.append(mat)
        
        test_data.append(data)


def get_mean(test_data,mean):
    s0=np.zeros((512,512))
    #print(test_data[0][9])
    for mode in range(n2-n1+1):
        s=np.zeros((512,512))
        for i in range(10):
            #print("mode",mode)
            #print("i",i)
            s+=test_data[mode][i]
        mean[mode+n1]=s/10
        filename="mean"+str(mode+n1)+".txt"
        #print(mean[mode+n1])
        print("mode",mode+n1,"\n",mean[mode+n1])
        np.savetxt(filename,list(mean[mode+n1]),fmt="%.2f")

def get_error(mat1,mat2):
    mat_d=abs(mat1-mat2)
    data=np.zeros((512,512))
    for i in range(512):
        for j in range(512):
            data[i][j]=mat_d[i][j]/mat1[i][j]
    return data

def process_error(data_error,threshold):
    data_t=np.zeros((512,512))
    for i in range(512):
        for j in range(512):
            if data_error[i][j]<threshold:
                data_t[i][j]=1
            else:
                data_t[i][j]=0
    data_count=np.zeros((512,512))
    count_error=0
    for i in range(511):
        for j in range(511):
            count=data_t[i][j]+data_t[i+1][j]+data_t[i][j+1]+data_t[i+1][j+1]
            if count<2:
                data_count=0
                count_error+=1
            else:
                data_count=1
    print(count_error)
                
    return data_count,count_error

def get_rio(mode_test,threshold,mode_base):
    mode=mode_test-n1
    for i in range(10):
        data_error=get_error(mean[mode_base],test_data[mode][i])
        data_count,count_error=process_error(data_error,threshold)
        print("mode_test: ",mode_test," count_error: ",count_error,"error_rio",count_error/512/512,"\n")
        print(data_error)
def get_mean_resize(mode,list1):
    s=np.zeros((512,512))
    for i in list1:
        s+=test_data[mode-n1][i]
    mean[mode]=s/(len(list1))

def get_mean_mean():
    for i in range(len(mean)):
        s=np.sum(mean[i+n1])
        mean_mean[i+n1]=s/512/512

#m>=3 p>=5
test_data=[]
test_data_dark=[]
inttime=500000#ns
inttimes=range(0,1000000,200000)#1s=1000000us 
#[0, 200000, 400000, 600000, 800000]
mode=0
i=0
dir1="IS_Data/Matrix_512x512_Line"
dir2=".txt"

mean={}
mean_mean={}
n1=26
n2=28
#import_data(test_data,n1,n2)

#get_mean(test_data,mean)
#print("mean14\n",mean[14])
#get_rio(26,0.02,26)