# import colorgram
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

import random
import turtle as t
from colors import color_list

t.colormode(255)

arrow = t.Turtle()
arrow.speed("fastest")
arrow.penup()
arrow.goto(-300, -300)
arrow.pendown()

def draw_row_of_dots(number_of_dots):
    for n in range(number_of_dots):
        arrow.dot(20, random.choice(color_list))
        if n < number_of_dots - 1:
            arrow.penup()
            arrow.forward(50)
            arrow.pendown()

def move_forward_without_drawing(length):
    arrow.penup()
    arrow.forward(length)
    arrow.pendown()

for row in range(1, 11):
    draw_row_of_dots(10)
    turn_direction = 90 if row % 2 == 0 else -90
    arrow.right(turn_direction)
    move_forward_without_drawing(50)
    arrow.right(turn_direction)

arrow.hideturtle()

screen = t.Screen()
screen.exitonclick()
