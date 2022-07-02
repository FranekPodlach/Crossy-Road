from turtle import Screen
from car import Car
from player import Player
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

screen.onkey(player.up, "Up")
cars = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    random_chance = random.randint(1, 6)
    if random_chance == 1 and len(cars) < 25:
        car = Car()
        cars.append(car)
    for car in cars:
        car.move()
        if player.ycor() > 290:
            for car in cars:
                car.next_level()
            scoreboard.next_level()
            player.goto(0, -300)
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()
        if car.xcor() < -350:
            car.hit_wall()


screen.exitonclick()