from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 270

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        

    def moveUp(self):
        self.forward(MOVE_DISTANCE)
        