# Ryan 
# Draw circles

from tkinter import N
import turtle
import random

t = turtle.Turtle()

def drawCircles():
    rad = 10
    n = 10
    for i in range(10):
        # # random color generator
        r = random.uniform(0.00,1.00)
        g = random.uniform(0.00,1.00)
        b = random.uniform(0.00,1.00)
        penRgb = [r,g,b]
        t.pencolor(penRgb[0], penRgb[1], penRgb[2])
        # random boolean to determine if filled or not
        # t.pencolor("orange")
        t.penup()
        t.goto(-100, -100+(rad*2*i))
        t.pendown()
        t.circle(rad)
        # t.circle(rad*i+10)
        t.penup()
drawCircles()

