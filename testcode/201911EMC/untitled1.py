# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:05:35 2019

@author: shadow
"""
import numpy as np
test_datas=np.loadtxt("test_datas.txt")
datat=test_datas;
for i in range(512):
    for j in range(512):
        if test_datas[i][j]<=0.05:
            datat[i][j]=1
        else:
            datat[i][j]=0
print (datat)
np.savetxt("datat.txt",datat)
datat2=datat
cout=0
for i in range(511):
    for j in range(511):
        n=datat[i][j]+datat[i+1][j]+datat[i][j+1]+datat[i+1][j+1]
        if n<2:
            datat2[i][j]=0
            cout+=1
        else:
            datat2[i][j]=1
            
print(datat2)
np.savetxt("datat2.txt",datat2)
print(cout)