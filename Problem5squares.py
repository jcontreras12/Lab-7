# Jose Contreras
# Date 11/13/21
# problem 5 use the chunks of code to produce the image shown below

import turtle
def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        t.hideturtle()

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
size = 25

for i in range(5):
    drawSquare(alex, size)
    size = size + 25
    alex.penup()
    alex.goto(alex.pos() + (-10, -10))
    alex.pendown()
wn.exitonclick()