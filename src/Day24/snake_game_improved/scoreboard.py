from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Consolas', 15, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
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
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.current_score = 0
        self.write_scoreboard_text()