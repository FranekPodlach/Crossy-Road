from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-290, 270)
        self.level = 1
        self.write(f"Level: {self.level}", False, "center", ("Courier", 25, "normal"))

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, "center", ("Courier", 25, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", ("Courier", 30, "normal"))