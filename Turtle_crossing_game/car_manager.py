from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.md = STARTING_MOVE_DISTANCE
        self.mi = MOVE_INCREMENT

    def generate(self):
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(stretch_len=2,stretch_wid=1)
        car.speed('fastest')
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.md)

    def level_up(self):
        self.md += self.mi

    
