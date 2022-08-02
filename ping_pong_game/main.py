from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Let's Play Ping Pong!")
screen.tracer(0)
screen.colormode(255)

player_one = Paddle()
player_one.goto(-350, 0)

player_two = Paddle()
player_two.goto(350, 0)

ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=player_two.go_up)
screen.onkey(key="Down", fun=player_two.go_down)
screen.onkey(key="w", fun=player_one.go_up)
screen.onkey(key="s", fun=player_one.go_down)

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    ball.move()

    # Detect collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with paddle
    if (
        ball.distance(player_two) < 50
        and ball.xcor() > 320
        or ball.distance(player_one) < 50
        and ball.xcor() < -320
    ):
        ball.x_bounce()

    # if ball.xcor() > 400 or ball.xcor() < -400:
    #     ball.setposition(ball.xcor(), ball.ycor())
    #     game_is_on = False


screen.exitonclick()
