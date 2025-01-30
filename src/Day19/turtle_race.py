import turtle as t
import random

colors = ["blue", "red", "brown", "green", "orange", "black"]

screen = t.Screen()
screen.setup(700, 500)
user_guess = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ").lower()

turtles = []
y_positions = [150, 100, 50, 0, -50, -100]
for i in range(6):
    turtle_obj = t.Turtle(shape="turtle")
    turtle_obj.color(colors[i])
    turtle_obj.penup()
    turtle_obj.setposition(-330, y_positions[i])
    turtles.append(turtle_obj)

has_race_finished = False
turtle_winner_color = ""

while not has_race_finished:
    for turtle in turtles:
        if turtle.xcor() >= 330:
            has_race_finished = True
            turtle_winner_color = turtle.pencolor()
            break

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if turtle_winner_color == user_guess:
    print(f"You have won! The {turtle_winner_color} turtle is the winner!")
else:
    print(f"You have lost! The {turtle_winner_color} turtle is the winner!")

screen.exitonclick()
