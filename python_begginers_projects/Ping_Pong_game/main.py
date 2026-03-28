from turtle import Turtle, Screen
from paddle import Paddle
from ball_class import Ball
from score import Score
import time

screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)



game_is_on = True

#paddle instance
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

r_score = Score("P2",(200,200))
l_score = Score("P1",(-200,200))
ball = Ball()


#Controls or right paddle
screen.onkey(key="Up",fun=r_paddle.goUP)
screen.onkey(key="Down",fun=r_paddle.goDOWN)

#control for left paddle
screen.onkey(key="w",fun=l_paddle.goUP)
screen.onkey(key="s",fun=l_paddle.goDOWN)

while game_is_on:
    #animation
    time.sleep(0.08)

    screen.update()
    screen.listen()
    
    #ball movement
    ball.move()

    #bounce logic
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y() 
    
    
    if ball.distance(r_paddle) < 65 and ball.xcor() > 320 or ball.distance(l_paddle) < 65 and ball.xcor() > -320:
        ball.bounce_x()

    # score tracker
    if ball.xcor() > 360:
        l_score.get_point()

    elif ball.xcor() <-360:
        r_score.get_point()

    # Ball reset
    if ball.xcor() > 361 or ball.xcor() < -361:
        ball.refresh()
    


screen.exitonclick()