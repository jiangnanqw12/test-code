import math
# 贷款总额
#T = 200*10000
T = 100*10000
# 贷款时间
#M = 30 * 12
M = 20 * 12
# 贷款年利率
#R = 5.45/100
R = 4/100

# 等额本金 Equal principal


def equal_principal():
    # 月利率
    r_permonth = R / 12
    # 每月应还本金
    principal = T / M
    # 每月还款结果
    res_arr = []
    for i in range(M):
        rest_total = T - i * principal
        rest_interest = rest_total * r_permonth
        m_permont = principal + rest_interest
        res_arr.append(round(m_permont, 2))
    total_m = sum(res_arr)
    print("还款总额:%d" % total_m)
    print("支付总利息:%d" % (total_m - T))
    print("首月还款:%d" % res_arr[0])
    print("每月还款递减:%d" % (principal * r_permonth))


# 等额本息
'''
每月还款计算公式
a = T* r * (1 + r)^M / (1 + r)^M -1
'''


def equal_cost():
    r = R / 12
    t = math.pow(1+r, M)
    a = round(T * r * t / (t - 1), 2)
    print("每月还款数额:%d元" % a)
    print("还款总额:%d元" % (a * M))
    print("支付的总利息:%d元" % ((a * M)-T))


if __name__ == "__main__":
    print("等额本金" + ("="*10))
    equal_principal()
    print("等额本息" + ("="*10))
    equal_cost()
