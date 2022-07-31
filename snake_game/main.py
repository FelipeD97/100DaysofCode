from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        # If snake head is within 15 pixels of the food then they've collided
        print("nom... nom... nom...")
        food.update()
        scoreboard.increase_score()

    # if snake.head.distance(screen) < 20:
    #     print("You crashed!\nGame Over")
    #     game_is_on = False


screen.exitonclick()
