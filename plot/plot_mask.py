import matplotlib.pyplot as plt
import matplotlib.patches as patches

# X2  X3
#   X
# X1  X4

# Rectangle
# Inkscape x2
# matplotlib x1

# Circle
# Inkscape x2
# the top-left point of the bounding box
# matplotlib x
# the circle's center

# 定义常量
# mm

# led_1
LED_1_X, LED_1_Y = 178.2, 40.524
LED_1_DIAMETER = 2

# glass_substrate_1
GLASS_SUBSTRATE_1_LENGTH = 152
GLASS_SUBSTRATE_1_WIDTH = 6.35
GLASS_SUBSTRATE_1_LED_1_DELTA_X = \
    - (GLASS_SUBSTRATE_1_LENGTH / 2 + 30 + 1.5 + LED_1_DIAMETER/2)
GLASS_SUBSTRATE_1_LED_1_DELTA_Y = (7 + GLASS_SUBSTRATE_1_WIDTH / 2)
GLASS_SUBSTRATE_1_X = GLASS_SUBSTRATE_1_LED_1_DELTA_X + LED_1_X
GLASS_SUBSTRATE_1_Y = GLASS_SUBSTRATE_1_LED_1_DELTA_Y + LED_1_Y

# protection_frame_1
PROTECTION_FRAME_1_LENGTH = 122
PROTECTION_FRAME_1_WIDTH = 6
PROTECTION_FRAME_1_LED_1_DELTA_X = \
    - (GLASS_SUBSTRATE_1_LENGTH / 2 + 30 + 1.5 + LED_1_DIAMETER/2)
PROTECTION_FRAME_1_LED_1_DELTA_Y = (7 - PROTECTION_FRAME_1_WIDTH / 2)
PROTECTION_FRAME_1_X = PROTECTION_FRAME_1_LED_1_DELTA_X + LED_1_X
PROTECTION_FRAME_1_Y = PROTECTION_FRAME_1_LED_1_DELTA_Y + LED_1_Y

# pin_1
PIN_1_LENGTH = 6
PIN_1_WIDTH = 2
PIN_1_LED_1_DELTA_X = -(PIN_1_WIDTH/2+1.5+2+30 +
                        GLASS_SUBSTRATE_1_LENGTH+30+1.5+LED_1_DIAMETER/2)
PIN_1_LED_1_DELTA_Y = 7+7
PIN_1_X = PIN_1_LED_1_DELTA_X+LED_1_X
PIN_1_Y = PIN_1_LED_1_DELTA_Y+LED_1_Y

# slot_height
SLOT_HEIGHT=19.05

class CircleComponentMatplotlib:
    def __init__(self, x, y, diameter, edgecolor='white', facecolor='white'):
        self.x = x
        self.y = y
        self.radius = diameter / 2
        self.edgecolor = edgecolor
        self.facecolor = facecolor

    def draw(self, ax):
        circle = patches.Circle((self.x, self.y), self.radius,
                                edgecolor=self.edgecolor, facecolor=self.facecolor)
        ax.add_patch(circle)


class RectangleComponentMatplotlib:
    def __init__(self, center_x, center_y, length, width, edgecolor='white', facecolor='black'):
        self.x = center_x - length / 2
        self.y = center_y - width / 2
        self.length = length
        self.width = width
        self.edgecolor = edgecolor
        self.facecolor = facecolor

    def draw(self, ax):
        rectangle = patches.Rectangle(
            (self.x, self.y), self.length, self.width, edgecolor=self.edgecolor, facecolor=self.facecolor)
        ax.add_patch(rectangle)

def main():
    # Create a plot
    fig, ax = plt.subplots()

    # Set plot limits and background color
    ax.set_xlim(-50, 200)
    ax.set_ylim(0, 100)
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_aspect('equal', adjustable='box')

    # Create the components
    led_1 = CircleComponentMatplotlib(LED_1_X, LED_1_Y, LED_1_DIAMETER)

    glass_substrate_1 = RectangleComponentMatplotlib(GLASS_SUBSTRATE_1_X, GLASS_SUBSTRATE_1_Y,
                                                    GLASS_SUBSTRATE_1_LENGTH, GLASS_SUBSTRATE_1_WIDTH)
    protection_frame_1 = RectangleComponentMatplotlib(PROTECTION_FRAME_1_X, PROTECTION_FRAME_1_Y,
                                                    PROTECTION_FRAME_1_LENGTH, PROTECTION_FRAME_1_WIDTH)
    pin_1 = RectangleComponentMatplotlib(PIN_1_X,    PIN_1_Y,
                                        PIN_1_WIDTH, PIN_1_LENGTH, facecolor='white'
                                        )



    # Draw the components
    led_1.draw(ax)
    glass_substrate_1.draw(ax)
    protection_frame_1.draw(ax)
    pin_1.draw(ax)

    # Hide the axes
    ax.axis('off')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()