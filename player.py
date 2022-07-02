from mimetypes import init
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        
    def up(self):
        self.goto(0, self.ycor() + 10)