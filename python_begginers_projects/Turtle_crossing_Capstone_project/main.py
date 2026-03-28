from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Score
import time



screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.tracer(0)



player = Player()
car = CarManager()
score = Score()

screen.listen()
screen.onkey(key="Up",fun=player.moveUp)

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()
    score.Levels()

    if player.ycor() >280:
        player.goto(x=0,y=-270)
        score.Levelled_up()
        car.levelup()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.gameover()


screen.exitonclick()