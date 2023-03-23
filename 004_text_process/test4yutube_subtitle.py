import os
path = "/mnt/d/BaiduNetdiskDownload/YouTube/Understanding Kalman Filters/"
f = open(path+"Understanding Kalman Filters, Part 1 Why Use Kalman Filters.txt")
linelist = f.readlines()
f2 = open(path+"t.txt", "w")
for line in linelist:
    if line != "\n":
        if line[-2] == "." or line[-2] == "?":
            print(line)
            f2.write(line)
