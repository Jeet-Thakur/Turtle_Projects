from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid = 0.5,stretch_len=4.5,outline=0)
        self.penup()
        self.speed("fastest")
        self.goto(x,y)


    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        self.setheading(270)
        self.forward(20)