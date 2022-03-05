fee=500000
s=0
for i in range(5):
    fee=fee-12*5000
    profit=fee*0.04
    fee+=profit
    print(profit)
    s+=profit
print(s)
