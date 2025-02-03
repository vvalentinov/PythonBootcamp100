from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Consolas", 15, "normal")
LEVEL_SCORE_COORDINATES = (-240, 260)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.current_level = 1
        self.penup()
        self.write_to_screen(f"Level: {self.current_level}", LEVEL_SCORE_COORDINATES)

    def write_to_screen(self, message, coordinates):
        self.goto(coordinates)
        self.write(message, False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.current_level += 1
        self.clear()
        self.write_to_screen(f"Level: {self.current_level}", LEVEL_SCORE_COORDINATES)
