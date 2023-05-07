import turtle
import math
colors = ["red", "purple", "blue", " green", "orange", "yellow"]
my_pen = turtle.Pen()
turtle.bgcolor('black')
my_pen.speed(200)
for x in range(360):
    my_pen.pencolor(colors[x % 6])
    my_pen.width(x*10/100 + 1)
    my_pen.left(97)
    my_pen.forward(x-10)
    my_pen.backward(x)
    my_pen.right(90)