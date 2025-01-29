import random
from turtle import Turtle, Screen

arrow = Turtle()
arrow.penup()
arrow.goto(-150, 300)
arrow.pendown()

screen = Screen()

for sides in range(3, 11):
    for n in range(sides):
        arrow.forward(200)
        arrow.right(360 / sides)
    arrow.color(random.random(), random.random(), random.random())

screen.exitonclick()
