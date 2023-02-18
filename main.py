import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#General screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# Player
player = Player()
screen.onkeypress(player.go_up, "Up")
screen.listen()
# CarManager
car_manager = CarManager()
# Scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect if player hits the top of the edge
    if player.ycor() >= player.finish_line_y:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.increase_speed()

    #Detect player-car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.mainloop()
screen.exitonclick()