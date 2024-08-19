from turtle import Turtle, Screen
import random

screen = Screen()
screen.delay(4)
allturtles = []

finishline = Turtle()
finishline.turtlesize(stretch_wid=100,stretch_len=0.2)
finishline.shape('square')
finishline.penup()
finishline.color('black')
finishline.goto(305, 0)

for i in range(5):
    allturtles.append(Turtle())

y = 200
a = 0

colors = ['red','blue','green','yellow','orange']

for i in allturtles:
    i.color(colors[a])
    i.penup()
    i.shape('turtle')
    i.turtlesize(stretch_wid = 2,stretch_len = 2)
    i.goto(-400,y)
    y-=75
    a+=1
flag = 0

bet = screen.textinput(title='the bet',prompt='enter your bet here')

while True:
    for i in allturtles:
        i.forward(random.randint(1,4))

        if i.xcor() >= 300:
            winner = i.color()
            flag = 1
            break
    if flag == 1:
        break

if winner[0] == bet:
    print(f'you win {winner[0]} is the winner')
else:
    print(f'you lose {winner[0]} is the winner')


screen.exitonclick()