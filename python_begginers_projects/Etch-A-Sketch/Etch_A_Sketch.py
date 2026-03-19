from turtle import Turtle, Screen
  
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(40)

def move_backwards():
    tim.backward(40)

def C_Clockwise():
    tim.setheading(tim.heading() - 10)


def Clockwise():
    tim.setheading(tim.heading() + 10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=C_Clockwise)
screen.onkey(key="d", fun=Clockwise)
screen.onkey(key="c", fun=clear_screen)



screen.exitonclick()