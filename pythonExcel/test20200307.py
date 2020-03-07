
def main():
    fee=getFeeNumber()
    for date in fee:
        print(date)
        print(fee[date])
        print("date:",date,"lunch:",fee[date][0],"dinner:",fee[date][1])
def getFree():

def getFeeNumber():
    f=open("data.txt","r")
    fee=dict()
    
    countDinner=0
    DinnerFlag=0
    countLunch=0
    LunchFlag=0
    while 1:
        line=f.readline()
        if not line:
            break
        # print(line)
        # print(type(line))
        
        if line[4]=="0" and line[5]=="1"  :
            
            MonthStr=line[0]+line[1]
            DayStr=line[2]+line[3]
            #month=eval(line[0]+line[1])
            
            #print(date)
            
            lunch=line[6]+line[7]
            feeLunch=eval(lunch)
            if feeLunch>0:
                countLunch+=1
                LunchFlag=1
            
            #print(lunch)
            dinner=line[10]+line[11]
            feeDinner=eval(dinner)
            if feeDinner>0:
                countDinner+=1
                DinnerFlag=1
            
            #print(dinner)
            
            
            fee[MonthStr+DayStr]=[feeLunch,feeDinner,LunchFlag,DinnerFlag]
            

        # for i in range(len(line)):

        #     print("i:",i," ","value:",line[i])
            
        # line2=line.decode()
        # print(line2)
        # print(type(line2))
        
    # line=f.readline()
    # print(line[0])

    f.close()
    return fee

main()