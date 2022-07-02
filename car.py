from turtle import Turtle, penup
import random

COLORS = ["red", "blue", "yellow", "pink", "black", "green", "purple", "orange"]
MOVE_INCREMENT = 3

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.turtlesize(1, 2, 1)
        self.goto(350, random.randint(-270, 270))
        self.speed_movement = 5

    def move(self):
        self.backward(self.speed_movement)

    def next_level(self):
        self.speed_movement += MOVE_INCREMENT
    
    def hit_wall(self):
        self.goto(350, random.randint(-270, 270))
        self.color(random.choice(COLORS))
        