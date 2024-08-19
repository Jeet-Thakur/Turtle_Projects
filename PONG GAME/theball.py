from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.goto(0,0)

    def start(self):
        self.setheading(random.randint(0,30))

    def keep_moving(self):
        self.forward(3)

    def bounce_top(self):
        angle = self.heading()
        if angle < 90:
            self.setheading(-angle)
        else:
            i = 180 - angle
            self.setheading(angle + 2*i)

    def bounce_bot(self):
        angle = self.heading()
        if angle > 270:
            self.setheading(angle + 2*(360 - angle))
        else:
            self.setheading(angle - 2*(90 - (270 - angle)))

    def bounce_right(self):
        angle = self.heading()
        if angle < 90:
            self.setheading(angle + 2*(90 - angle))
        else:
            self.setheading(angle - 2*(90 - (360 - angle)))

    def bounce_left(self):
        angle = self.heading()
        if angle > 180:
            self.setheading(angle + 2*(90 - (angle - 180)))
        else:
            self.setheading(angle - 2*(90 - (180 - angle)))