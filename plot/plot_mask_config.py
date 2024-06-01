import matplotlib.pyplot as plt
import matplotlib.patches as patches
import yaml

# 加载配置文件
with open('parameters.yaml', 'r') as file:
    params = yaml.safe_load(file)

# 从配置文件中提取参数
led_1 = params['led_1']['circle']
glass_substrate_1_delta = params['glass_gubstrate_1_led_1_delta']['delta']
glass_substrate_1 = params['glass_substrate_1']['rectangle']
protection_frame_1_delta = params['protection_frame_1_led_1_delta']['delta']
protection_frame_1 = params['protection_frame_1']['rectangle']

# 计算中心点坐标
delta_x_1, delta_y_1 = glass_substrate_1_delta
delta_x2_1, delta_y2_1 = protection_frame_1_delta
center_x_1 = delta_x_1 + led_1['center'][0]
center_y_1 = delta_y_1 + led_1['center'][1]
center_x_2 = delta_x2_1 + led_1['center'][0]
center_y_2 = delta_y2_1 + led_1['center'][1]

# 创建一个绘图区域
fig, ax = plt.subplots()

# 设置绘图区域范围
ax.set_xlim(0, 400)
ax.set_ylim(0, 100)

# 设置背景颜色为黑色
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# 设置轴比例为相等
ax.set_aspect('equal', adjustable='box')

# led_1 circle
led_1_circle = patches.Circle(led_1['center'], led_1['diameter'] / 2, edgecolor=led_1['stroke'], facecolor=led_1['fill'])
ax.add_patch(led_1_circle)

# glass_substrate_1 rectangle
glass_substrate_1_rect = patches.Rectangle(
    (center_x_1 - glass_substrate_1['dimensions'][0] / 2, center_y_1 - glass_substrate_1['dimensions'][1] / 2),
    glass_substrate_1['dimensions'][0], glass_substrate_1['dimensions'][1], edgecolor=glass_substrate_1['stroke'], facecolor=glass_substrate_1['fill']
)
ax.add_patch(glass_substrate_1_rect)

# protection_frame_1 rectangle
protection_frame_1_rect = patches.Rectangle(
    (center_x_2 - protection_frame_1['dimensions'][0] / 2, center_y_2 - protection_frame_1['dimensions'][1] / 2),
    protection_frame_1['dimensions'][0], protection_frame_1['dimensions'][1], edgecolor=protection_frame_1['stroke'], facecolor=protection_frame_1['fill']
)
ax.add_patch(protection_frame_1_rect)

# 隐藏坐标轴
ax.axis('off')

# 显示图形
plt.show()
