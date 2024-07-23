import numpy as np
import matplotlib.pyplot as plt

# 参数设置
fs = 100000  # 采样率（Hz）
f = 10000    # 信号频率（Hz）
duration = 0.01  # 信号持续时间（秒），足以捕获完整的周期
t = np.arange(0, duration, 1/fs)  # 时间向量

# 生成带偏置的正弦波信号
A = 2.5  # 幅值
offset = 2.5  # 偏置
noise = 0.1 * np.random.normal(size=len(t))  # 加入一些噪声
signal = A * np.sin(2 * np.pi * f * t) + offset + noise

# 应用快速傅里叶变换 (FFT)
n = len(t)
fft_result = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(n, 1/fs)

# 找到主要频率的幅度
fft_mag = np.abs(fft_result)[:n // 2] * 2 / n  # 双侧频谱转单侧
peak_freq = np.argmax(fft_mag)
main_amplitude = fft_mag[peak_freq] - offset  # 减去偏置得到真实幅值

# 打印和可视化结果
print(f"主要频率为: {fft_freq[peak_freq]} Hz")
print(f"对应的幅值为: {main_amplitude} V")

# 绘制原始信号和FFT结果
plt.figure(figsize=(12, 6))

#plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.title("Original Signal")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.ylim(-10,10)
plt.show()
#plt.subplot(1, 2, 2)
plt.stem(fft_freq[:n // 2], fft_mag, linefmt="b-", markerfmt="bo", basefmt="r-")
plt.title("FFT of the Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, 3 * f)

plt.tight_layout()
plt.show()