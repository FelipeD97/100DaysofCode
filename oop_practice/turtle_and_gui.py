from turtle import Turtle, Screen, setheading
import random


timmy = Turtle()

# 1) Draw a Square

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# 2) Draw a Dashed Line

# for _ in range(10):
#     timmy.fd(10)
#     timmy.penup()
#     timmy.fd(10)
#     timmy.pendown()

# 3) Drawing Different Shapes

# num_sides = 3


# def create_shape(num_sides):
#     degree = 360 / num_sides
#     timmy.pencolor(random.random(), random.random(), random.random())
#     for _ in range(num_sides):
#         timmy.right(degree)
#         timmy.fd(100)


# while num_sides < 11:

#     create_shape(num_sides)
#     num_sides += 1

# 4) Generate a Random Walk

# possible_moves = [0, 90, 180, 270]

# timmy.pensize(10)

# for _ in range(200):
#     timmy.pencolor(random.random(), random.random(), random.random())
#     timmy.forward(30)
#     timmy.setheading(random.choice(possible_moves))
#     timmy.speed("fastest")

# 5) Draw a Spirograph

timmy.speed("fastest")


def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        timmy.pencolor(random.random(), random.random(), random.random())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

my_screen = Screen()
my_screen.exitonclick()
