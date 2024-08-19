from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen = Screen()
screen.title('the snake game')
screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.tracer(0)

snake = Snake()
snake.make_snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.move_up,'w')
screen.onkey(snake.move_left,'a')
screen.onkey(snake.move_right,'d')
screen.onkey(snake.move_down,'s')

game_on = True

while game_on:
    screen.update()
    time.sleep(0.08)

    snake.move()
    
    if food.distance(snake.mysnake[0]) < 15:
        food.refresh()
        score.increase_score()
        snake.snake_grow()

    # DETECTING collision with the wall

    if snake.mysnake[0].xcor() > 280 or snake.mysnake[0].xcor() < -280 or snake.mysnake[0].ycor() > 280 or snake.mysnake[0].ycor() < -280:
        # game_on = False
        snake.snake_reset()
        score.reset_score()
        snake.make_snake()
        # score.game_over()

    # body collision
    for segment in snake.mysnake[1:]:
        if segment.distance(snake.mysnake[0]) < 10:
            snake.snake_reset()
            score.reset_score()
            snake.make_snake()

screen.exitonclick()