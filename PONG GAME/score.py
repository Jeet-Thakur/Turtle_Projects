from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.r_score = -5
        self.l_score = -5

    def write_r_score(self):
        self.clear()
        self.goto(100,250)
        self.r_score+=5
        self.write(f'{self.r_score}', align='center', font=('Arial',80,'normal'))

    def write_l_score(self):
        self.clear()
        self.goto(-100,250)
        self.l_score+=5
        self.write(f'{self.l_score}', align='center', font=('Arial',80,'normal'))

    def game_over(self,stri):
        self.write(f"GAME OVER.\n {stri}",move=False,align='center',font=("arial",25,"normal"))

        