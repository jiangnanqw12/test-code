# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:19:33 2019

@author: shadow
"""

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
s31=np.zeros((512,512))
print(mean3)
for i in range(5):
    s31+=test_data[0][i]
mean31=s31/5

s32=np.zeros((512,512));
for i in range(5,10):
    s32+=test_data[0][i]
mean32=s32/5

mode=1
s5=sum(test_data[1])

mean5=s5/10
print(mean5)

means=abs(mean3-mean5)

print(means)
np.savetxt("mean31.txt",mean31)
np.savetxt("mean32.txt",mean32)
