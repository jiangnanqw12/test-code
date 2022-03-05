
"""
Created on Fri Jan 12 11:29:01 2020

@author: jiangn3617
"""


import numpy as np
import matplotlib.pyplot as plt


def check_483_data(data):
    counter_Right=0
    counter_Error=0
    for i in range(512):
        compare=0

        for j in range(512):
            if compare!=data[i][j]:
                print('error')
                counter_Error+=1
                break
                break
            compare+=2
        counter_Right+=1
        #print(couter)
    if counter_Error>0 &counter_Right==512:
        print("the data must be checked")
    if counter_Error==0&counter_Right<512:
        print("Test 483 Pass")

def load_data():

    #order=input("please input your file name or order\n")#Python3
    order=raw_input("please input your file name or order\n")#Python2
    #filename="Matrix_512x512_Line2_10000_0.txt"
    #print(type(order))
    #print(order)
    #path="..\\..\\00record\\CMOStest\\200420\\" #coms test
    path="~/SMEE/bin/vxworks/"
    print()
    if order=="IS" or order=="is":
        filename="Matrix_512x512_Line99_1000_99.txt"
        print("Matrix_512x512_Line99_1000_99.txt,\nfilename")
    elif order[0]=="M" and order[1]=="a" and order[2]=="t" and order[3]=="r" and order[4]=="i"  and order[5]=="x" and order[-1]=="t":
        filename=order
        print("\nfilename\n",order,"\n")
    else:
        print("error,the filename if incorrect")
    data = np.loadtxt(path+filename)
    return data

def data_plot(data):

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

def main():
    data=load_data()
    print(data)
    check_483_data(data)

if __name__=="__main__":
    main()





