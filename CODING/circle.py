from turtle import *
from colorsys import *

# Setup screen
setup(800, 800)
bgcolor("black")
speed(0)
tracer(False)   # smoother drawing

pensize(2)
h = 0

def draw(ang, n):
    circle(20 + n * 2, 90)    # larger arcs
    left(ang)
    circle(40 + n * 1.5, 90)  # bigger, smoother arcs

up()
goto(0, 50)
down()

# Main loop
for i in range(360):
    col = hsv_to_rgb(h, 1, 1)
    color(col)
    h += 0.0028  # slower rainbow shift
    
    draw(60, i)
    draw(180, i/2)
    left(10)     # spiral twist
    
    if i % 5 == 0:   # refresh every few steps
        update()

hideturtle()
done()
