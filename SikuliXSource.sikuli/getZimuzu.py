#coding:utf-8
import sys

print(sys.version)
# SeedPath="C:/sikulix-2.0.3/seed.txt"
SeedPath = "C:/Users/shade/Documents/GitHub/testCode/SikuliXSource.sikuli/seed.txt"
file = open(SeedPath ,"r")#encoding="utf-8"
for line in file.readlines():
    click(Region(622,80,72,26))#click download offline
    click(Region(725,415,111,17))#click fit
   

    name = line.decode(encoding='UTF-8')
    
    paste(name)
    click(Region(1011,559,81,33)) #start to download
    wait(10)
    click(Region(1031,616,69,24))  #download background
    
