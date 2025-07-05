import turtle
from turtle import Turtle

import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
states_names = data["state"].to_list()
guessed_state = []
while len(guessed_state) <50:
    guess = screen.textinput(title= "0/50 States", prompt="What's another state's name?").title()
    missing_states = []
    for state in states_names:
        if state not in guessed_state:
            missing_states.append(state)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")

    if guess == "Exit":
        break
    if guess in states_names:
        guessed_state.append(guess)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(guess)






