import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# guessed_state = state_data[state_data["state"] == answer_state.title()]

correct_guesses = []
score = 0
is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess the State", prompt="What's another state's name?").title()
    # state_title = answer_state.title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()

        state_data = data[data.state == answer_state]
        new_state.goto(int(state_data.x), int(state_data.y))
        new_state.write(answer_state)
        correct_guesses.append(answer_state)
        score += 1
    else:
        is_game_on = False


