import math
# 目前，上海首套房贷执行利率：LPR(4.3%)+35bp =4.65%，二套房贷执行利率：LPR(4.3%)+105bp=5.35%。
buchong = 1914*6+2764*6
gongji = 2678*6+3870*6
gongzi = 19487.95+42674.99+17293.82+18722.82+18559.82+14940.02 + \
    13107.62+24866.42+12208.52+15483.62+11739.16+11707.12
print("总收入：", buchong+gongji+gongzi)
print(gongzi)
# 房价
house = 2865139
shoufubili = 0.33
print("房子总价:", house)
print("首付:", shoufubili*house)
gongjijin = 600000
print("公积金贷款:", gongjijin)
shangyedai = house*(1-shoufubili)-gongjijin
print("商业贷款:", house*(1-shoufubili)-gongjijin)
# 贷款总额
#T = 200*10000
#T = house*(1-shoufubili)
# 贷款时间
#M = 30 * 12
M = 20 * 12
# 贷款年利率
#R = 5.45/100

shangyedai_lilv = 4.65/100
gongjijin_lilv = 3.1/100
# 等额本金 Equal principal


def equal_principal(T, R=4.95/100):
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
    return total_m, res_arr[0]


# 等额本息
'''
每月还款计算公式
a = T* r * (1 + r)^M / (1 + r)^M -1
'''


def equal_cost(T, R=4.9/100):
    r = R / 12
    t = math.pow(1+r, M)
    a = round(T * r * t / (t - 1), 2)
    print("每月还款数额:%d元" % a)
    print("还款总额:%d元" % (a * M))
    print("支付的总利息:%d元" % ((a * M)-T))
    return a * M, a


if __name__ == "__main__":
    print("公积金")
    print("等额本金" + ("="*10))
    gjjtotal, gjjper = equal_principal(gongjijin, gongjijin_lilv)
    print("等额本息" + ("="*10))
    gjjtotal2, gjjper2 = equal_cost(gongjijin, gongjijin_lilv)
    print("商业贷")
    print("等额本金" + ("="*10))
    total, per = equal_principal(shangyedai, shangyedai_lilv)
    print("等额本息" + ("="*10))
    total2, per2 = equal_cost(shangyedai, shangyedai_lilv)

    print("还款总额", total2+gjjtotal2)
    print("还款总额", total+gjjtotal)
    print("还款每月", per2+gjjper2)
    print("还款每月", per+gjjper)
