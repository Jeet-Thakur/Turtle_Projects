from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        self.myscore = 0
        self.file = open('data.txt',mode='r+')
        self.highscore = int(self.file.read())
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.write(f'SCORE : {self.myscore} HIGH SCORE : {self.highscore}',False,'center', font=('Courier',15,'normal'))

    def increase_score(self):
        self.clear()
        self.myscore+=5
        self.write(f'SCORE : {self.myscore} HIGH SCORE : {self.highscore}',False,'center', font=('Courier',15,'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over.',False,'center', font=('Courier',15,'normal'))

    def reset_score(self):
        if self.myscore > self.highscore:
            self.highscore = self.myscore
            self.file.seek(0)
            self.file.write(str(self.highscore))
        self.myscore = 0
        self.clear()
        self.write(f'SCORE : {self.myscore} HIGH SCORE : {self.highscore}',False,'center', font=('Courier',15,'normal'))

