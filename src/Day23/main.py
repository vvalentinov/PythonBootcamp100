from turtle import Screen
from turtle_player import TurtlePlayer
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = TurtlePlayer()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.write_to_screen("Game Over", (0, 0))

    if player.ycor() > 280:
        player.reset_player()
        car_manager.level_up()
        scoreboard.update_scoreboard()

screen.exitonclick()