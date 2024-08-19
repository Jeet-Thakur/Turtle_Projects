def moveright():
    turtle.forward(5)

def moveleft():
    turtle.forward(-5)

def turnup():
    turtle.rt(5)

def turndown():
    turtle.lt(5)

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=500)
screen.bgcolor("white")

turtle = Turtle()
turtle.speed(30)
turtle.color('red')
turtle.pensize(10)

screen.listen()
screen.onkeypress(moveright,'d')
screen.onkeypress(moveleft,'a')
screen.onkeypress(turnup,'w')
screen.onkeypress(turndown,'s')



screen.exitonclick()
