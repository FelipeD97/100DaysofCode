from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Let's Play Ping Pong!")
screen.tracer(0)
screen.colormode(255)

l_paddle = Paddle()
l_paddle.goto(-350, 0)

r_paddle = Paddle()
r_paddle.goto(350, 0)

ball = Ball()

scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # Detect collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with paddle
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.x_bounce()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()
