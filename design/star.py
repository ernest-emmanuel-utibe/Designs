# Defined function
from turtle import *
import turtle as t


def my_turtle():
    # Choices
    sides = str(3)
    loops = str(450)
    pen = 1
    # Loop
    for i in range(int(loops)):
        forward(i * 2 / int(sides) + i)
        left(360 / int(sides) + .350)
        hideturtle()
        pensize(pen)
        speed(30)
        left(90)


my_turtle()
t.done()
