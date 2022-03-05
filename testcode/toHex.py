import numpy as np
import matplotlib.pyplot as plt

order=input("please input your file name or order\n")#Python3
#order=raw_input("please input your file name or order\n")#Python2
#filename="Matrix_512x512_Line2_10000_0.txt"
print(type(order))
print(order)

if order=="IS" or order=="is":
    filename="Matrix_512x512_Line99_1000000_99.txt"
    print("Matrix_512x512_Line99_1000000_99.txt,\nfilename")
elif order[0]=="M" and order[1]=="a" and order[2]=="t" and order[3]=="r" and order[4]=="i"  and order[5]=="x" and order[-1]=="t":
    filename=order
    print("\nfilename\n",order,"\n")
else:
    print("error,the filename if incorrect")

data = np.loadtxt(filename)
data2=data.tobytes()
#print(data2)
np.savetxt("data2.txt",data2)