import matplotlib.pyplot as plt
import matplotlib.patches as patches

"""
X2  X3
  X
X1  X4

Rectangle
Inkscape x2
matplotlib x1

Circle
Inkscape x2
the top-left point of the bounding box
matplotlib x
the circle's center
"""

# Configuration constants front_view (all lengths are in mm)

TUBAN = 6
OTHER_SLOT_HEIGHT = 19.05

LED_1_X, LED_1_Y, LED_1_Z = 150, 50, 0
LED_1_DIAMETER = 2

TUBAN_ZAIWAI_DELTA_Z = 50

GLASS_SUBSTRATE_1_LENGTH = 152
GLASS_SUBSTRATE_1_WIDTH = 152
GLASS_SUBSTRATE_1_HEIGHT = 6.35
GLASS_SUBSTRATE_1_LED_1_DELTA_X = -(GLASS_SUBSTRATE_1_LENGTH / 2 + 30 + 1.5 + LED_1_DIAMETER / 2)
GLASS_SUBSTRATE_1_LED_1_DELTA_Y = 7 + GLASS_SUBSTRATE_1_HEIGHT / 2
GLASS_SUBSTRATE_1_LED_1_DELTA_Z = TUBAN + GLASS_SUBSTRATE_1_WIDTH / 2
GLASS_SUBSTRATE_1_X = GLASS_SUBSTRATE_1_LED_1_DELTA_X + LED_1_X
GLASS_SUBSTRATE_1_Y = GLASS_SUBSTRATE_1_LED_1_DELTA_Y + LED_1_Y
GLASS_SUBSTRATE_1_Z = GLASS_SUBSTRATE_1_LED_1_DELTA_Z + LED_1_Z

PROTECTION_FRAME_1_LENGTH = 122
PROTECTION_FRAME_1_WIDTH = 149
PROTECTION_FRAME_1_HEIGHT = 6
PROTECTION_FRAME_1_LED_1_DELTA_Y = 7 - PROTECTION_FRAME_1_HEIGHT / 2

PROTECTION_FRAME_1_X = GLASS_SUBSTRATE_1_X
PROTECTION_FRAME_1_Y = PROTECTION_FRAME_1_LED_1_DELTA_Y + LED_1_Y
PROTECTION_FRAME_1_Z = GLASS_SUBSTRATE_1_Z

PIN_1_LENGTH = 6
PIN_1_WIDTH = 2
PIN_1_HEIGHT = 6
PIN_1_LED_1_DELTA_X = -(PIN_1_WIDTH / 2 + 1.5 + 2 + 30 + GLASS_SUBSTRATE_1_LENGTH + 30 + 1.5 + LED_1_DIAMETER / 2)
PIN_1_LED_1_DELTA_Y = 7 + 7
PIN_1_X = PIN_1_LED_1_DELTA_X + LED_1_X
PIN_1_Y = PIN_1_LED_1_DELTA_Y + LED_1_Y
PIN_1_Z = LED_1_Z


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


def plot_front_view_mask(ax, slot_height, num_components):
    """Plot the front view (XY) mask with the given slot height and number of components."""
    for i in range(num_components):
        led = LED(LED_1_X, LED_1_Y - i * slot_height, LED_1_DIAMETER)
        glass_substrate = GlassSubstrate(GLASS_SUBSTRATE_1_X, GLASS_SUBSTRATE_1_Y - i * slot_height,
                                         GLASS_SUBSTRATE_1_LENGTH, GLASS_SUBSTRATE_1_HEIGHT)
        protection_frame = ProtectionFrame(PROTECTION_FRAME_1_X, PROTECTION_FRAME_1_Y - i * slot_height,
                                           PROTECTION_FRAME_1_LENGTH, PROTECTION_FRAME_1_HEIGHT)
        pin = Pin(PIN_1_X, PIN_1_Y - i * slot_height, PIN_1_WIDTH, PIN_1_LENGTH, facecolor='white')

        led.draw(ax)
        glass_substrate.draw(ax)
        protection_frame.draw(ax)
        pin.draw(ax)

    led_mapping = LED(LED_1_X, LED_1_Y + slot_height, LED_1_DIAMETER, facecolor='red')
    led_mapping.draw(ax)


def plot_top_view_mask(ax):
    """Plot the top view (XZ) mask with the given slot height and number of components."""

    led = LED(LED_1_X, LED_1_Z, LED_1_DIAMETER)
    led2 = LED(LED_1_X, LED_1_Z + TUBAN_ZAIWAI_DELTA_Z, LED_1_DIAMETER)
    glass_substrate = GlassSubstrate(GLASS_SUBSTRATE_1_X, GLASS_SUBSTRATE_1_Z,
                                     GLASS_SUBSTRATE_1_LENGTH, GLASS_SUBSTRATE_1_WIDTH)
    protection_frame = ProtectionFrame(PROTECTION_FRAME_1_X, PROTECTION_FRAME_1_Z,
                                       PROTECTION_FRAME_1_LENGTH, PROTECTION_FRAME_1_WIDTH)
    pin = Pin(PIN_1_X, PIN_1_Z, PIN_1_WIDTH, PIN_1_LENGTH, facecolor='white')
    pin2 = Pin(PIN_1_X, PIN_1_Z + TUBAN_ZAIWAI_DELTA_Z, PIN_1_WIDTH, PIN_1_LENGTH, facecolor='white')
    led.draw(ax)
    led2.draw(ax)
    glass_substrate.draw(ax)
    protection_frame.draw(ax)
    pin.draw(ax)
    pin2.draw(ax)


def create_combined_fig():
    """Create a combined figure with two subplots and save as an SVG file."""
    xlim = (-72.8, 152)
    ylim = (-47.5, 74)
    zlim = (-6, 200)

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Set plot limits and background color for front view
    ax = axs[0]
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_aspect('equal', adjustable='box')
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

    # Plot the front view mask
    plot_front_view_mask(ax, OTHER_SLOT_HEIGHT, 6)
    ax.axis('off')

    # Set plot limits and background color for top view
    ax = axs[1]
    ax.set_xlim(xlim)
    ax.set_ylim(zlim)
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_aspect('equal', adjustable='box')

    # Plot the top view mask
    plot_top_view_mask(ax)
    ax.axis('off')

    # Save the plot as an SVG file
    plt.savefig("C:\\output\\view_masks_combined.svg", format="svg")

    # Show the plot (optional)
    plt.show()


def create_separate_figs():
    """Create separate figures for front and top views and save each as an SVG file."""
    xlim = (-72.8, 152)
    ylim = (-47.5, 74)
    zlim = (-6, 200)

    # Front view figure
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_aspect('equal', adjustable='box')
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plot_front_view_mask(ax, OTHER_SLOT_HEIGHT, 6)
    ax.axis('off')
    plt.savefig("C:\\output\\front_view_mask.svg", format="svg")
    plt.show()

    # Top view figure
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(xlim)
    ax.set_ylim(zlim)
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_aspect('equal', adjustable='box')
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plot_top_view_mask(ax)
    ax.axis('off')
    plt.savefig("C:\\output\\top_view_mask.svg", format="svg")
    plt.show()

def main():
    """Main function to create and save the plot as an SVG file."""
    # Create combined figure with both views
    create_combined_fig()

    # Create separate figures for each view
    create_separate_figs()

if __name__ == "__main__":
    main()