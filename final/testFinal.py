from py5canvas import *
import math
import cmath

# Parameters
a = -0.89567065
b = 1.5909586
c = 1.8525863
d = -2.1974306
e = 2.1
f = .70

# Initial point
x = .1
y = 0.2
z = 0.25


def setup():
    create_canvas(1000, 1000)
    background(255)
    stroke(0)
    stroke_weight(1)

def draw():
    global x, y, z

    # Draw many points each frame
    for _ in range(50):

        # Calculate next point
        x_new = math.sin(a * y) - math.cos(b * x) * math.tan(cmath.pi + z) 
        y_new = math.sin(c / x) - math.cos(c * y) / math.sin(x / d) / math.ceil(math.pi) 
        z_new = math.sin(e * z) - math.cos(c * f) / math.tan(e * d) - math.ceil(f)
       
        x, y, z = x_new, y_new, z_new

        # Map coordinates from [-2,2] to the canvas
        sx = remap(y, -10, 10, 0, width)
        sy = remap(x, -10, 10, height, 5)
        

        point(sx, sy)

    for _ in range(50):

        # Calculate next point
        x_new = math.sin(a * y) - math.cos(b * x) * math.tan(cmath.pi / z) 
        y_new = math.sin(c * x) - math.cos(c * y) / math.sin(x - d) / math.ceil(math.pi) 
        z_new = math.sin(f / z) - math.cos(c * f) / math.tan(e * d) - math.ceil(f)
       
        x, y, z = x_new, y_new, z_new

        # Map coordinates from [-2,2] to the canvas
        sx = remap(y, -10, 10, 0, width/2)
        sy = remap(x, -10, 10, height, 5)
        

        point(sx, sy)
    for _ in range(50):

        # Calculate next point
        x_new = math.sin(a * c) - math.cos(b * x) * math.tan(cmath.pi * z) 
        y_new = math.sin(c * x) - math.cos(d * f) / math.sin(x / d) 
        z_new = math.sin(e * z) - math.cos(c * f) / math.tan(e * d) - math.ceil(f)
       
        x, y, z = x_new, y_new, z_new

        # Map coordinates from [-2,2] to the canvas
        sx = remap(y, -10, 10, 0, width*1.5)
        sy = remap(x, -10, 10, height, 5)
        

        point(sx, sy)

run()
