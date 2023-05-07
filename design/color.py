import turtle
import colorsys

touch_pen = turtle.Turtle()
screen = turtle.Screen().bgcolor('black')
touch_pen.speed(0)
number = 70
hold = 0
for the_integer in range(360):
    create = colorsys.hsv_to_rgb(hold, 1, 0.8)
    hold += 1 / number
    touch_pen.color(create)
    touch_pen.left(1)
    touch_pen.fd(1)
    for the_next_integer in range(2):
        touch_pen.left(2)
        touch_pen.circle(100)