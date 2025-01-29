from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()

arrow.color("red")

for _ in range(30):
    arrow.forward(10)
    arrow.penup()
    arrow.forward(5)
    arrow.pendown()

screen.exitonclick()
