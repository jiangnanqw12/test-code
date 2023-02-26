# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:44:11 2019

@author: shadow
"""
import numpy as np
mean3=np.loadtxt("mean3.txt")
means=np.loadtxt("means.txt")

test_datas=[]
for i in range(512):
    data=[]
    for j in range(512):
        data.append(means[i][j]/mean3[i][j])
    test_datas.append(data)
print(test_datas)

np.savetxt("test_datas.txt",test_datas)
