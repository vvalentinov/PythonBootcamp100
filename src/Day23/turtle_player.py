from turtle import Turtle

STARTING_POSITION = (0, -280)

class TurtlePlayer(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(10)

    def reset_player(self):
        self.goto(STARTING_POSITION)
