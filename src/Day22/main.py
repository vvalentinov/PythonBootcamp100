from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_up, key="w")
screen.onkey(left_paddle.go_down(), "s")
screen.onkeypress(left_paddle.go_down, key="s")

screen.onkey(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_up, key="Up")
screen.onkey(right_paddle.go_down(), "Down")
screen.onkeypress(right_paddle.go_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(right_paddle) < 50 and
            ball.xcor() > 320 or
            ball.distance(left_paddle) < 50 and
            ball.xcor() < -320):
        ball.bounce_x()

    # Detect if right paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect if left paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()