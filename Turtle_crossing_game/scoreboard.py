from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.levelboard = Turtle()
        self.levelboard.hideturtle()
        self.levelboard.penup()
        self.levelboard.goto(-260, 260)
        self.level = 0

    def game_over(self):
        over = Turtle()
        over.hideturtle()
        over.penup()
        over.write("Game Over.",move=False,align='center',font=FONT)

    def level_up(self):
        self.level+=1
        self.levelboard.clear()
        self.levelboard.write(f'Level : {self.level}',move=False,align='left',font=FONT)
