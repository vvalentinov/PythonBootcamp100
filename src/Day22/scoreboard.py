from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def write_text(self, text):
        self.write(text, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write_text(self.left_score)
        self.goto(100, 200)
        self.write_text(self.right_score)

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()
