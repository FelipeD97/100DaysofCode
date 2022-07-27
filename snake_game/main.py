from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game!")
screen.tracer(0)


snake_body = 3
starting_position = 0

segments = []

for square in range(0, snake_body):
    square = Turtle(shape="square")
    square.color("white")
    square.penup()
    square.setposition(starting_position, 0)
    starting_position -= 20
    segments.append(square)


game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    for segment in range(len(segments) - 1, 0, -1):
        new_x = segments[segment - 1].xcor()
        new_y = segments[segment - 1].ycor()
        segments[segment].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()
