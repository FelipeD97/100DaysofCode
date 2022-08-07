from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("snake_game/highscore.txt", mode="r") as file:
    contents = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(contents)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("snake_game/highscore.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def update_scoreboard(self):
        self.clear()
        self.write(
            arg=f"Current Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
