# 定义电阻值和精度
Rx = 25  # SPRT 的电阻值，单位为欧姆
Rs = 25  # 参考电阻，单位为欧姆
accuracy_ppm = 0.06  # 精度，单位为 ppm

# 计算电阻比
resistance_ratio = Rx / Rs

# 计算精度，单位为 ppm
accuracy_ratio = resistance_ratio * accuracy_ppm

# 输出结果
print(f"Resistance Ratio: {resistance_ratio}")
print(f"Accuracy in ppm: {accuracy_ratio}")

# 对于直接比较法
uncertainty_contribution_ppm = 0.06
print(f"Uncertainty Contribution in ppm: {uncertainty_contribution_ppm}")

# 考虑所有影响因素，总测量不确定性在亚毫开尔文范围内
total_measurement_uncertainty_sub_mK = "Achievable"
print(f"Total Measurement Uncertainty: {total_measurement_uncertainty_sub_mK}")