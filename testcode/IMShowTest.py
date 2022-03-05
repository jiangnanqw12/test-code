#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

import sys

if __name__=="__main__":
    if len(sys.argv)<2:
        print("please select data_file.")
        exit()
    filename = sys.argv[1]
    
    print(filename)
    data = np.loadtxt(filename)
    plt.imshow(data)
    plt.title(filename.split("/")[-1]+"_max_"+str(data.max()))
    plt.colorbar()

    plt.show()
