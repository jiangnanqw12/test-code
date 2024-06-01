import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
led_1_x, led_1_y = 178.2, 40.524
led_1_diameter = 2
led_1_circle = patches.Circle((led_1_x, led_1_y), led_1_diameter / 2, edgecolor='white', facecolor='white')
ax.add_patch(led_1_circle)

# glass_substrate_1 rectangle
delta_x_1, delta_y_1 = (30 + 1 + 152 / 2), (7 + 6.35 / 2)
center_x_1, center_y_1 = (delta_x_1 + led_1_x), (delta_y_1 + led_1_y)
glass_substrate_1_rect = patches.Rectangle(
    (center_x_1 - 152 / 2, center_y_1 - 6.35 / 2), 152, 6.35, edgecolor='white', facecolor='black'
)
ax.add_patch(glass_substrate_1_rect)

# protection_frame_1 rectangle
delta_x2_1, delta_y2_1 = (30 + 1 + 152 / 2), (7 - 6 / 2)
center_x_2, center_y_2 = (delta_x2_1 + led_1_x), (delta_y2_1 + led_1_y)
protection_frame_1_rect = patches.Rectangle(
    (center_x_2 - 122 / 2, center_y_2 - 6 / 2), 122, 6, edgecolor='white', facecolor='black'
)
ax.add_patch(protection_frame_1_rect)

# 隐藏坐标轴
ax.axis('off')

# 显示图形
plt.show()
