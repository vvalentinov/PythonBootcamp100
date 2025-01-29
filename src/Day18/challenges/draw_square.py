from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("blue")

for _ in range(4):
    turtle.forward(200)
    turtle.right(90)

screen.exitonclick()
