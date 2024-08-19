import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.level_up()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True

carcount = 0
carcheck = 6

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_car()

    #generate car
    if carcount < carcheck:
        carcount+=1
    else:
        car_manager.generate()
        carcount = 0

    # detect collision

    for car in car_manager.cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    for i in range(len(car_manager.cars) - 1):
        if car_manager.cars[i].xcor() < -330:
            car_manager.cars.pop(i)

    # check for level clearance
    if player.ycor() > 280:
        player.next_lvl()
        scoreboard.level_up()
        car_manager.level_up()
        carcheck-=1


screen.exitonclick()