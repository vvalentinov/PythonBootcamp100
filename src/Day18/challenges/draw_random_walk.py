import random
import turtle as t

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue

t.colormode(255)

turtle_tim = t.Turtle()
turtle_tim.pensize(13)
turtle_tim.speed("fast")

screen = t.Screen()

for _ in range(100):
    turtle_tim.setheading(random.choice([0, 90, 180, 270]))
    turtle_tim.forward(random.randint(10, 50))
    turtle_tim.color(random_color())

screen.exitonclick()
