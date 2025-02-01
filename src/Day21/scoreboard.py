from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Consolas', 15, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.penup()
        self.write_scoreboard_text()
        self.hideturtle()

    def update_score(self):
        self.current_score += 1
        self.write_scoreboard_text()

    def write_scoreboard_text(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.current_score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align=ALIGNMENT, font=FONT)