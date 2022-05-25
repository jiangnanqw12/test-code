x = 500000
gain = 0
n = 5
for i in range(n):
    x = (x-12*5000)
    g = x*0.035
    gain += g
    print(i+1, " ", g, " ", gain)
