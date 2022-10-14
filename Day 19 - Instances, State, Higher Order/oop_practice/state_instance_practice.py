from turtle import Turtle, Screen

tony = Turtle()
screen = Screen()


def move_forward():
    tony.fd(10)


def move_backward():
    tony.backward(10)


def turn_left():
    # tony.heading() + 10
    tony.left(10)
    tony.forward(10)


def turn_right():
    # tony.heading() - 10
    tony.right(10)
    tony.forward(10)


def clear():
    tony.clear()
    tony.penup()
    tony.home()
    tony.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
