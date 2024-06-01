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

# Configuration constants (all lengths are in mm)
LED_1_X, LED_1_Y = 178.2, 40.524
LED_1_DIAMETER = 2

GLASS_SUBSTRATE_1_LENGTH = 152
GLASS_SUBSTRATE_1_WIDTH = 6.35
GLASS_SUBSTRATE_1_LED_1_DELTA_X = -(GLASS_SUBSTRATE_1_LENGTH / 2 + 30 + 1.5 + LED_1_DIAMETER / 2)
GLASS_SUBSTRATE_1_LED_1_DELTA_Y = 7 + GLASS_SUBSTRATE_1_WIDTH / 2
GLASS_SUBSTRATE_1_X = GLASS_SUBSTRATE_1_LED_1_DELTA_X + LED_1_X
GLASS_SUBSTRATE_1_Y = GLASS_SUBSTRATE_1_LED_1_DELTA_Y + LED_1_Y

PROTECTION_FRAME_1_LENGTH = 122
PROTECTION_FRAME_1_WIDTH = 6
PROTECTION_FRAME_1_LED_1_DELTA_X = -(GLASS_SUBSTRATE_1_LENGTH / 2 + 30 + 1.5 + LED_1_DIAMETER / 2)
PROTECTION_FRAME_1_LED_1_DELTA_Y = 7 - PROTECTION_FRAME_1_WIDTH / 2
PROTECTION_FRAME_1_X = PROTECTION_FRAME_1_LED_1_DELTA_X + LED_1_X
PROTECTION_FRAME_1_Y = PROTECTION_FRAME_1_LED_1_DELTA_Y + LED_1_Y

PIN_1_LENGTH = 6
PIN_1_WIDTH = 2
PIN_1_LED_1_DELTA_X = -(PIN_1_WIDTH / 2 + 1.5 + 2 + 30 + GLASS_SUBSTRATE_1_LENGTH + 30 + 1.5 + LED_1_DIAMETER / 2)
PIN_1_LED_1_DELTA_Y = 7 + 7
PIN_1_X = PIN_1_LED_1_DELTA_X + LED_1_X
PIN_1_Y = PIN_1_LED_1_DELTA_Y + LED_1_Y

SLOT_HEIGHT = 19.05

class CircleComponentMatplotlib:
    def __init__(self, x, y, diameter, edgecolor='white', facecolor='white'):
        self.x = x
        self.y = y
        self.radius = diameter / 2
        self.edgecolor = edgecolor
        self.facecolor = facecolor

    def draw(self, ax):
        """Draw the circle on the given axes."""
        circle = patches.Circle((self.x, self.y), self.radius, edgecolor=self.edgecolor, facecolor=self.facecolor)
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
        """Draw the rectangle on the given axes."""
        rectangle = patches.Rectangle((self.x, self.y), self.length, self.width, edgecolor=self.edgecolor, facecolor=self.facecolor)
        ax.add_patch(rectangle)

class LED(CircleComponentMatplotlib):
    pass

class GlassSubstrate(RectangleComponentMatplotlib):
    pass

class ProtectionFrame(RectangleComponentMatplotlib):
    pass

class Pin(RectangleComponentMatplotlib):
    pass

def main(slot_height=SLOT_HEIGHT):
    """Main function to create and display the plot."""
    fig, ax = plt.subplots()

    # Set plot limits and background color
    ax.set_xlim(-50, 200)
    ax.set_ylim(-100, 100)
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_aspect('equal', adjustable='box')

    # Create and draw components
    for i in range(6):
        led = LED(LED_1_X, LED_1_Y - i * slot_height, LED_1_DIAMETER)
        glass_substrate = GlassSubstrate(GLASS_SUBSTRATE_1_X, GLASS_SUBSTRATE_1_Y - i * slot_height,
                                         GLASS_SUBSTRATE_1_LENGTH, GLASS_SUBSTRATE_1_WIDTH)
        protection_frame = ProtectionFrame(PROTECTION_FRAME_1_X, PROTECTION_FRAME_1_Y - i * slot_height,
                                           PROTECTION_FRAME_1_LENGTH, PROTECTION_FRAME_1_WIDTH)
        pin = Pin(PIN_1_X, PIN_1_Y - i * slot_height, PIN_1_WIDTH, PIN_1_LENGTH, facecolor='white')

        led.draw(ax)
        glass_substrate.draw(ax)
        protection_frame.draw(ax)
        pin.draw(ax)

    # Hide the axes and show the plot
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
