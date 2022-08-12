import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_name = turtle.Turtle()
state_name.hideturtle()

data = pandas.read_csv("us-states-game-start/50_states.csv")
all_states = data.state.to_list()

answers = []

while len(answers) < 50:

    answer_state = screen.textinput(
        title=f"Guess the State ({len(answers)}/50)",
        prompt="What's another state name?",
    )

    capital_state = answer_state.title()

    for state in all_states:

        if capital_state == state:
            correct_state = data[data.state == capital_state]
            state_name.penup()
            state_name.goto(int(correct_state.x), int(correct_state.y))
            state_name.write(capital_state)
            if capital_state not in answers:
                answers.append(capital_state)
