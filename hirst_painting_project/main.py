# import colorgram

# image = "/Users/Flip/Desktop/100 Days of Code/hirst_painting_project/image.jpg"

# rgb_colors = []
# colors = colorgram.extract(image, 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)

# print(rgb_colors)

from turtle import Turtle, Screen
import random

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

point = Turtle()

my_screen = Screen()
my_screen.colormode(255)


point.penup()
point.setheading(225)
point.forward(300)
point.setheading(0)
point.pendown()


row = 1

while row <= 10:

    for _ in range(10):
        point.dot(20, random.choice(color_list))
        point.penup()
        point.fd(50)
        point.pendown()

    point.penup()
    point.setheading(90)
    point.forward(50)
    point.setheading(180)
    point.forward(500)
    point.setheading(0)
    point.pendown()

    row += 1


my_screen.exitonclick()
