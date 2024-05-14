## 专业技能
编程语言: 熟练使用 C/C++/Python/MATLAB，具有多年代码编写及调试经验。
数学基础: 具有较为扎实的数学知识 (线代/微积分/多元微积分等方面)
语言能力: 无障碍阅读外文文献，无字幕可听懂大部分英文音频, 口语满足日常交流需求；
传感器: 调试过压力传感器、CMOS、激光、雷达等传感器;
操作系统: 具有在 Linux/Vxworks/RTT 操作系统下编程经验；
驱动开发: 熟悉 PCI/PCIe/RS232 驱动开发;
嵌入式开发: 拥有 STM32/DSP 开发经验，独立进行板卡原理图设计及布线调试
图形工具: 熟练使用 mermaid,drawio 等工具绘制流程图;
图像识别: 有 OpenCV 使用经验，熟悉 Feature2D 特征识别，推导过 Canny、Harris、Hough、SIFT、FAST 等算法的数学原理及算法的复现;
点云处理: 有 PCL 库使用经验，复现过 RANSAC 平面分割、KD-Tree 聚合算法
有 TensorFlow 库使用经验，复现过基础神经网络的搭建和反向传播的数学原理;

## 工作经历
### 医疗器材公司
负责超声刀的 DSP 底层驱动和控制算法开发。
### 上海微电子装备集团
成像系统模块负责人
1. 管理 CMOS 驱动板卡、LVDS 转光纤板卡、光纤转 PCI 板卡的 FPGA 与原理图维护
2. 开发 VxWorks 下的驱动测试代码
3. 使用 Python 和 MATLAB 进行仿真测试

驱动与固件开发工程师
1. 开发 VxWorks 下的 PCIe 和 PCI 驱动代码
2. 协助 FPGA 代码开发
3. 在 DSP 上开发仿真算法

算法与测校开发
1. 在 VxWorks 下开发算法计算模块和业务流程代码
2. 在 Linux 下开发测校应用

## 学校项目
### 触点材料检测系统
1. 设计并实现控制板卡的原理图绘制、布线和焊接。
2. 开发 stm32 MCU 主控逻辑，驱动力学、电压电流等传感器。
3. 处理传感器数据，并集成 Labview 前端平台。
4. 对于材料表面缺陷识别，利用 DOG 对于特征点检测，利用 SIFT 对于材料表面特征的描述与追踪,SIFT 算法复现及数学原理推导。
5. 构建神经网络，基于接触电阻、质量等参数作为材料失效模型的判断依据，对实验数据打标签，反向传播，基于梯度方向训练