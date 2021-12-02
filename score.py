from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 28, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        """self.high_score = 0"""
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(-50, 270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} \tHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def count(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
