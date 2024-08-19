from turtle import Turtle
class Snake:
    def __init__(self):
        self.mysnake = []
        self.shift = 0

    def make_snake(self):
        for i in range(3):
            part = Turtle()
            part.shape('square')
            part.color('white')
            part.penup()
            part.teleport(self.shift-21,0)
            self.mysnake.append(part)
            self.shift -= 21

    def snake_grow(self):
        xcor = self.mysnake[-1].xcor()
        ycor = self.mysnake[-1].ycor()
        part = Turtle()
        part.shape('square')
        part.color('white')
        part.penup()
        part.goto(xcor,ycor)
        self.mysnake.append(part)


    def move(self):
        for segno in range(len(self.mysnake)-1, 0, -1):
            xcor = self.mysnake[segno-1].xcor()
            ycor = self.mysnake[segno-1].ycor()
            self.mysnake[segno].goto(xcor,ycor)

        self.mysnake[0].forward(15)

    def move_up(self):
        if self.mysnake[0].heading() != 270:
            self.mysnake[0].setheading(90)

    def move_left(self):
        if self.mysnake[0].heading() != 0:
            self.mysnake[0].setheading(180)


    def move_right(self):
        if self.mysnake[0].heading() != 180:
            self.mysnake[0].setheading(0)

    def move_down(self):
        if self.mysnake[0].heading() != 90:
            self.mysnake[0].setheading(-90)

    def snake_reset(self):
        for part in self.mysnake:
            part.goto(-1000,-1000)
        self.mysnake.clear()
