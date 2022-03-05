# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 11:29:01 2019

@author: jiangn3617
"""

#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

order=input("please input your file name or order\n")#Python3
#order=raw_input("please input your file name or order\n")#Python2
#filename="Matrix_512x512_Line2_10000_0.txt"
print(type(order))
print(order)

if order=="IS" or order=="is":
    filename="/home/is01/SMEE/bin/vxworks/Matrix_512x512_Line99_1000000_99.txt"
    print("Matrix_512x512_Line99_1000000_99.txt,\nfilename")
elif order[0]=="M" and order[1]=="a" and order[2]=="t" and order[3]=="r" and order[4]=="i"  and order[5]=="x" and order[-1]=="t":
    filename="/home/is01/SMEE/bin/vxworks/"+order
    print("\nfilename\n",order,"\n")
else:
    print("error,the filename if incorrect")
data = np.loadtxt(filename)
#plt.colorbar()
plt.subplot(1,2,1)
plt.imshow(data,'gray')
plt.title('gray')
plt.subplot(1,2,2)
plt.imshow(data)
plt.title('normal')
print("please notice")
print(data)
plt.show()

