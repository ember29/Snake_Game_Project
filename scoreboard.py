
from turtle import Turtle
ALIGNMENT = "center"
FONT=("Arial",15,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("White")
        self.pu()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"score:{self.score}",True,align=ALIGNMENT,font=FONT)

    def score_inc(self):
        self.clear()
        self.goto(0,270)
        self.score=self.score+1
        self.write(f"score:{self.score}", True, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.",True,align=ALIGNMENT,font=FONT)