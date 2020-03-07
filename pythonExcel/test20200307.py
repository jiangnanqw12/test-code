
f=open("data.txt","r")
while 1:
    line=f.readline()
    if not line:
        break
    print(line[0])
    print(type(line))
    if line[4]=="0"&line[5]=="1"&line[8]=="0"&line[9]=="2"&line[12]=="0"&line[13]=="3":
        date=line[0]+line[1]+line[2]+line[3]
        lunch=line[6]+line[7]
        dinner=line[10]+line[10]
    for i in range(len(line)):

        print("i:",i," ","value:",line[i])
        
    # line2=line.decode()
    # print(line2)
    # print(type(line2))
    
# line=f.readline()
# print(line[0])

f.close()