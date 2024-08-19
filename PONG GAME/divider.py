from turtle import Turtle

class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.pensize(10)
        self.penup()
        self.goto(0,-355)
        self.setheading(90)
        self.speed(100)


    def draw_line(self):
        while self.ycor() < 355:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(25)
