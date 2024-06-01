import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 定义常量
LED_1_X, LED_1_Y = 178.2, 40.524
LED_1_DIAMETER = 2

GLASS_SUBSTRATE_1_LENGTH = 152
GLASS_SUBSTRATE_1_WIDTH = 6.35
GLASS_SUBSTRATE_1_LED_1_delta_x=-(30 + 1 + GLASS_SUBSTRATE_1_LENGTH / 2)
GLASS_SUBSTRATE_1_LED_1_delta_y=(7 + GLASS_SUBSTRATE_1_WIDTH / 2)
GLASS_SUBSTRATE_1_x=(GLASS_SUBSTRATE_1_LED_1_delta_x + LED_1_X)
GLASS_SUBSTRATE_1_y=GLASS_SUBSTRATE_1_LED_1_delta_y + LED_1_Y
PROTECTION_FRAME_1_LENGTH = 122
PROTECTION_FRAME_1_WIDTH = 6

# 创建一个绘图区域
fig, ax = plt.subplots()

# 设置绘图区域范围
ax.set_xlim(-50, 200)
ax.set_ylim(0, 100)

# 设置背景颜色为黑色
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# 设置轴比例为相等
ax.set_aspect('equal', adjustable='box')

# led_1 circle
led_1_circle = patches.Circle((LED_1_X, LED_1_Y), LED_1_DIAMETER / 2, edgecolor='white', facecolor='white')
ax.add_patch(led_1_circle)

# glass_substrate_1 rectangle
delta_x_1, delta_y_1 = -(30 + 1 + GLASS_SUBSTRATE_1_LENGTH / 2), (7 + GLASS_SUBSTRATE_1_WIDTH / 2)
center_x_1, center_y_1 = (delta_x_1 + LED_1_X), (delta_y_1 + LED_1_Y)
glass_substrate_1_rect = patches.Rectangle(
    (GLASS_SUBSTRATE_1_x - GLASS_SUBSTRATE_1_LENGTH / 2, GLASS_SUBSTRATE_1_y - GLASS_SUBSTRATE_1_WIDTH / 2), GLASS_SUBSTRATE_1_LENGTH, GLASS_SUBSTRATE_1_WIDTH, edgecolor='white', facecolor='black'
)
ax.add_patch(glass_substrate_1_rect)

# protection_frame_1 rectangle
delta_x2_1, delta_y2_1 = -(30 + 1 + PROTECTION_FRAME_1_LENGTH / 2), (7 - PROTECTION_FRAME_1_WIDTH / 2)
center_x_2, center_y_2 = (delta_x2_1 + LED_1_X), (delta_y2_1 + LED_1_Y)
protection_frame_1_rect = patches.Rectangle(
    (center_x_2 - PROTECTION_FRAME_1_LENGTH / 2, center_y_2 - PROTECTION_FRAME_1_WIDTH / 2), PROTECTION_FRAME_1_LENGTH, PROTECTION_FRAME_1_WIDTH, edgecolor='white', facecolor='black'
)
ax.add_patch(protection_frame_1_rect)

# 隐藏坐标轴
ax.axis('off')

# 显示图形
plt.show()
