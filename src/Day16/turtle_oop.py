from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("coral")

timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)

my_screen = Screen()

print(f"Height: {my_screen.canvheight}")
print(f"Width: {my_screen.canvwidth}")

my_screen.exitonclick()