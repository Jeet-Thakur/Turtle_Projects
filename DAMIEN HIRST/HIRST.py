from turtle import Screen,Turtle
import random

def r_color():
    color = []
    for i in range(3):
        color.append(random.choice(range(256)))
    return '#%02x%02x%02x' % tuple(color)

rows = 12
cols = 11

screen = Screen()
screen.bgcolor('white')
screen.setup(width=800, height=600)
screen.delay(0)
jeet = Turtle()
jeet.hideturtle()
jeet.speed(300)
jeet.teleport(-220,-220)



for i in range(rows):
    jeet.dot(30,r_color())
    for j in range(cols):
        jeet.penup()
        jeet.forward(40)
        jeet.pendown()
        jeet.dot(30,r_color())

    jeet.penup()
    jeet.goto(jeet.xcor() - 40*(rows - 1), jeet.ycor()+40)


print(jeet.pos())

screen.exitonclick()