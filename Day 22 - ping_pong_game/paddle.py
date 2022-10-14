from turtle import Turtle
import random

STARTING_POINTS = [(0, 0), (-20, 0), (-40, 0)]

color_list = [
    (239, 236, 238),
    (238, 237, 236),
    (237, 237, 241),
    (25, 108, 164),
    (194, 38, 81),
    (238, 161, 49),
    (234, 215, 85),
    (226, 237, 228),
    (223, 137, 176),
    (144, 108, 56),
    (102, 197, 219),
    (206, 166, 29),
    (20, 57, 132),
    (214, 73, 90),
    (239, 89, 50),
    (141, 208, 227),
    (118, 192, 140),
    (3, 186, 176),
    (106, 107, 199),
    (138, 29, 73),
    (4, 161, 86),
    (98, 51, 36),
    (22, 156, 210),
    (232, 165, 184),
    (175, 185, 221),
    (29, 90, 95),
    (233, 172, 161),
    (152, 213, 190),
    (242, 205, 8),
    (89, 48, 31),
]

MOVE_SPEED = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color(random.choice(color_list))

    def go_up(self):
        new_y = self.ycor() + MOVE_SPEED
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_SPEED
        self.goto(self.xcor(), new_y)
