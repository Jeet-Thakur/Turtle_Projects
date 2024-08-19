from turtle import Screen
from divider import Divider
from paddle import Paddle
from theball import Ball
from score import Score
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=1000, height=700)

screen.tracer(0)

divider = Divider()
divider.draw_line()

playerA = Paddle(470,0)
playerB = Paddle(-470,0)
A_score = Score()
A_score.write_r_score()
B_score = Score()
B_score.write_l_score()


ball = Ball()
ball.start()

screen.listen()
screen.onkeypress(playerA.move_up, "Up")
screen.onkeypress(playerA.move_down,"Down")
screen.onkeypress(playerB.move_up, "w")
screen.onkeypress(playerB.move_down,"s")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.01)

    ball.keep_moving()

    if ball.ycor() > 330:
        ball.bounce_top()
    elif ball.ycor() < -330:
        ball.bounce_bot()

    # check for paddle hit
    if ball.distance(playerA) < 50 and ball.xcor() > 460:
        ball.bounce_right()
        A_score.write_r_score()

    elif ball.distance(playerB) < 50 and ball.xcor() < -460:
        ball.bounce_left()
        B_score.write_l_score()

    #detect gameover sequence
    if ball.xcor() > 480 :
        game_on = False
        divider.clear()
        a = Score()
        a.game_over('Left Wins.')

    elif ball.xcor() < -480:
        game_on = False
        divider.clear()
        a = Score()
        a.game_over('Right Wins.')


screen.exitonclick()