from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 260)
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
