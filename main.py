import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
state_data = pandas.read_csv("50_states.csv")

guessed_state = state_data[state_data["state"] == answer_state.title()]
print(guessed_state)
