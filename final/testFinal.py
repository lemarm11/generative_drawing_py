from py5canvas import *
import math

# Parameters
a = 2.0
b = 4.5
c = 2.5
d = 1.0

# Initial point
x = 0.1
y = 0.2

def setup():
    create_canvas(800, 800)
    background(255)
    stroke(0)
    stroke_weight(1)

def draw():
    global x, y

    # Draw many points each frame
    for _ in range(1000):

        # Calculate next point
        x_new = math.sin(a * y) - math.cos(b * x)
        y_new = math.sin(c * x) - math.cos(d * y)

        x, y = x_new, y_new

        # Map coordinates from [-2,2] to the canvas
        sx = remap(x, -2, 2, 0, width)
        sy = remap(y, -2, 2, height, 0)

        point(sx, sy)

run()
