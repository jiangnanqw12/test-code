


def main():
    fee=dict()
    fee=getFeeNumber()
    for date in fee:
        print(date)
        print(fee[date])
        print("date:",date,"lunch:",fee[date][0],"dinner:",fee[date][1])
    FreeFeeTotal,FeeTotal=getFree(fee)
    for key in FreeFeeTotal:
        print("key:",key,"FreeFeeTotal:",FreeFeeTotal[key])
    for key in FeeTotal:
        print("key:",key,"FeeTotal:",FeeTotal[key])
def getFree(fee):
    _FreeFee=27
    FreeFeeTotal=dict()
    FeeTotal=dict()
    for i in range(12):
        FreeFeeTotal[i+1]=0
        FeeTotal[i+1]=0
    for date in fee:
        #print(1)
        month=int(date[0]+date[1])
        day=int(date[2]+date[3])
        #print(month)
        #print(day)
        if int(day)<=25:
            FeeTotal[month]=FeeTotal[month]+fee[date][0]+fee[date][1]
            if fee[date][2]==1:
                FreeFeeTotal[month]+=27
            if fee[date][3]==1:
                FreeFeeTotal[month]+=27
        else:
            FeeTotal[month+1]=FeeTotal[month+1]+fee[date][0]+fee[date][1]
            if fee[date][2]==1:

                FreeFeeTotal[month+1]+=27
            if fee[date][3]==1:


                FreeFeeTotal[month+1]+=27
    return FreeFeeTotal,FeeTotal

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
            #month=int(line[0]+line[1])

            #print(date)

            lunch=line[6]+line[7]
            feeLunch=int(lunch)
            if feeLunch>0:
                countLunch+=1
                LunchFlag=1
            #print(lunch)
            dinner=line[10]+line[11]
            feeDinner=int(dinner)
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