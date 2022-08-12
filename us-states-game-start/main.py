import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("us-states-game-start/50_states.csv")
all_states = data.state.to_list()

guessed_states = []

player_name = screen.textinput(title="Guess the State", prompt="What is your name?")

while len(guessed_states) < 50:

    answer_state = screen.textinput(
        title=f"Correct States ({len(guessed_states)}/50)",
        prompt="What's another state name?",
    )

    capitalized_state = answer_state.title()

    if capitalized_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(f"us-states-game-start/{player_name}StatesToLearn.csv")
        break

    if capitalized_state in all_states:
        correct_state = data[data.state == capitalized_state]
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(int(correct_state.x), int(correct_state.y))
        state_name.write(capitalized_state)
        if capitalized_state not in guessed_states:
            guessed_states.append(capitalized_state)
