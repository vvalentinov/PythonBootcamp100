import turtle as t

arrow = t.Turtle()
screen = t.Screen()

arrow.pensize(5)
arrow.shapesize(3)

t.listen()

def move_forward():
    arrow.fd(5)

def move_backwards():
    arrow.bk(5)

def turn_left():
    arrow.left(5)

def turn_right():
    arrow.right(5)

def clear_screen():
    # arrow.reset()
    arrow.clear()
    arrow.penup()
    arrow.goto(0, 0)
    # arrow.home()
    arrow.pendown()

t.onkey(key="w", fun=move_forward)
t.onkeypress(key="w", fun=move_forward)
t.onkey(key="W", fun=move_forward)
t.onkeypress(key="W", fun=move_forward)

t.onkey(key="s", fun=move_backwards)
t.onkeypress(key="s", fun=move_backwards)
t.onkey(key="S", fun=move_backwards)
t.onkeypress(key="S", fun=move_backwards)

t.onkey(key="a", fun=turn_left)
t.onkeypress(key="a", fun=turn_left)
t.onkey(key="A", fun=turn_left)
t.onkeypress(key="A", fun=turn_left)

t.onkey(key="d", fun=turn_right)
t.onkeypress(key="d", fun=turn_right)
t.onkey(key="D", fun=turn_right)
t.onkeypress(key="D", fun=turn_right)

t.onkey(key="c", fun=clear_screen)
t.onkey(key="C", fun=clear_screen)

screen.exitonclick()