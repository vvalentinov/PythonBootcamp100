import turtle
import pandas

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

correct_guesses = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"Guess the state {len(correct_guesses)}/50", prompt="What's another state name?").lower()
    if answer_state == "exit":
        break
    state = data[data.state.str.lower() == answer_state]
    if len(state) > 0:
        x_coordinate = int(state.x.iloc[0])
        y_coordinate = int(state.y.iloc[0])
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(x_coordinate, y_coordinate)
        state_turtle.write(answer_state.title())
        correct_guesses.append(answer_state.title())

missing_states_names_list = data[~data.state.isin(correct_guesses)].state.tolist()
missing_states_dataframe = pandas.DataFrame(missing_states_names_list)
missing_states_dataframe.to_csv("states_to_learn.csv")
