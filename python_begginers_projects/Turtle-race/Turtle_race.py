from turtle import Screen, Turtle
import random

screen = Screen()

screen.setup(width=500,height=400)
race_on = False
users_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race (red/blue/purple/cyan/yellow/orange)? Enter a color:").lower()

colors = ["red","blue","orange","yellow","cyan","purple"]
all_turtle = []

# print(users_bet)

y_positions = [-100 ,-50, 0 ,50 , 100 ,150]

for num_of_turtle in range(0 ,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[num_of_turtle])
    new_turtle.goto(x= -230 , y= y_positions[num_of_turtle])
    all_turtle.append(new_turtle)

if users_bet:
    race_on = True
    

while race_on:
     for turtle in all_turtle:
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if users_bet == winning_color:
                print(f"You've won , {winning_color} won the race heres a thumbs up as ur prize 👍")
            else:
                print(f"You've lost , {winning_color} won the race, You owe us 50 bucks 🗿")


   



screen.exitonclick()