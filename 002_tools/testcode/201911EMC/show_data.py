#Program a function that returns a new distribution 
#q, shifted to the right by U units. If U=0, q should 
#be the same as p.


import numpy as np



#data=np.loadtxt("IS_Data/Matrix_512x512_Line1_10000_0.txt")

test_data=[]
inttime=10000#ns
mode=0
i=0
dir1="IS_Data/Matrix_512x512_Line"
dir2=".txt"
for mode in [3,5]:
    data=[]
    for i in range(10):
        mat=np.loadtxt(dir1+str(mode)+"_"+str(inttime)+"_"+str(i)+dir2)
        data.append(mat)
    
    test_data.append(data)

mode=0
s3=sum(test_data[0])

mean3=s3/10
print(mean3)


mode=1
s5=sum(test_data[1])

mean5=s5/10
print(mean5)

means=abs(mean3-mean5)

print(means)
np.savetxt("mean3.txt",mean3)
np.savetxt("means.txt",means)
