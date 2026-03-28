from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

#Objects in game
snake = Snake()
food = Food()
score = Score()

# Screen activities
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

# flag
game_is_on = True

#game loop

while game_is_on:
   screen.update() #aninmation
   time.sleep(0.1)
   
   snake.move()


    #collision with food
   if snake.head.distance(food) < 15:
      food.refresh()
      score.increase_score()
      snake.extend()
    
    #COlission with tail
   for segments in snake.segments[1:]:
    if snake.head.distance(segments) < 10:
         game_is_on = False
         score.gameOver()
         score.endnote()
      
           
        
screen.exitonclick()
