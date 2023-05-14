import turtle
from turtle import *

# setting the screen for drawing
scr = turtle.Screen()
# Defining the instance of turtle
ttloo = turtle.Turtle()
speed(20)

# keeping the pen up initially
ttloo.penup()
ttloo.goto(-150, 125)
ttloo.pendown(
)

# Drawing the Orange Rectangle first
# and then the white rectangle
ttloo.color("orange")
ttloo.begin_fill()
ttloo.forward(400)
ttloo.right(90)
ttloo.forward(84)
ttloo.right(90)
ttloo.forward(400)
ttloo.end_fill()
ttloo.left(90)
ttloo.forward(84)

# now drawing the Green Rectangle
ttloo.color("green")
ttloo.begin_fill()
ttloo.forward(84)
ttloo.left(90)
ttloo.forward(400)
ttloo.left(90)
ttloo.forward(84)
ttloo.end_fill()

# Drawing the central Big Blue Circle
ttloo.penup()
ttloo.goto(35, 0)
ttloo.pendown()
ttloo.color("navy")
ttloo.begin_fill()
ttloo.circle(35)
ttloo.end_fill()

# Drawing the in-circle Big White Circle
ttloo.penup()
ttloo.goto(30, 0)
ttloo.pendown()
ttloo.color("white")
ttloo.begin_fill()
ttloo.circle(30)
ttloo.end_fill()

# Drawing the inside Mini Blue Circles of Flag
ttloo.penup()
ttloo.goto(-27, -4)
ttloo.pendown()
ttloo.color("navy")
for j in range(24):
    ttloo.begin_fill()
    ttloo.circle(2)
    ttloo.end_fill()
    ttloo.penup()
    ttloo.forward(7)
    ttloo.right(15)
    ttloo.pendown()

# drawing the Smaller Blue Circle
ttloo.color("navy")
ttloo.penup()
ttloo.goto(10, 0)
ttloo.pendown()
ttloo.begin_fill()
ttloo.circle(10)
ttloo.end_fill()

# Drawing the 24 spokes of the Indian Flag
ttloo.penup()
ttloo.goto(0, 0)
ttloo.pendown()
ttloo.pensize(1)
for j in range(24):
    ttloo.forward(30)
    ttloo.backward(30)
    ttloo.left(15)

# Drawing the stick of the Indian flag
ttloo.color("Brown")
ttloo.pensize(10)
ttloo.penup()
ttloo.goto(-150, 125)
ttloo.right(180)
ttloo.pendown()
ttloo.forward(500)

# to hide the turtle pen we used hideturtle
ttloo.hideturtle()
# holding the output on the window
turtle.done()