import random
import turtle as t

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue

t.colormode(255)
arrow = t.Turtle()
arrow.speed("fastest")

angle = 0
while angle <= 360:
    arrow.color(random_color())
    arrow.circle(100)
    angle += 5
    arrow.setheading(angle)

screen = t.Screen()
screen.exitonclick()
