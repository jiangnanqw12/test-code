x = 20


def get_fee(x):

    data = 16+12*2.5+(x-15)*2.5*1.5
    print(data)
    data2 = 16+12*2.5*1.3+(x-15)*2.5*1.5*1.3
    #data2 = 16+12*3.1+(x-15)*4.7

    print(data2)
    data3 = 16 + 12 * 2.5 + (x - 15) * 3.6
    print(data3)


# 188 #241
# get_fee(20)
get_fee(53)
