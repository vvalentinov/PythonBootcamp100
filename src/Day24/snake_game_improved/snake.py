from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.squares_list = []
        self.create_snake()
        self.head = self.squares_list[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        square = Turtle(shape="square")
        square.color("light green")
        square.penup()
        square.goto(position)
        self.squares_list.append(square)

    def extend(self):
        self.add_segment(self.squares_list[-1].position())

    def reset(self):
        for segment in self.squares_list:
            segment.goto(1000, 1000)
        self.squares_list.clear()
        self.create_snake()
        self.head = self.squares_list[0]

    def move(self):
        # range(start position, stop position, step)
        for sqr_num in range(len(self.squares_list) - 1, 0, -1):
            new_x = self.squares_list[sqr_num - 1].xcor()
            new_y = self.squares_list[sqr_num - 1].ycor()
            self.squares_list[sqr_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

