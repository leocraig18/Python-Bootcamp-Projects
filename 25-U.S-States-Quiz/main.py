import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []


def new_state(states, x, y):
    state = turtle.Turtle()
    state.penup()
    state.hideturtle()
    state.goto(x, y)
    state.write(states)


while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="What's another state's"
                                                                                              " name?")).title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        new_state(answer_state, int(state_data.x), int(state_data.y))


screen.exitonclick()

names = ["Leo, Josh, Steven, Seb"]
