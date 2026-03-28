from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=0.9)
        self.position  = ()
        self.goto(x=position[0],y=position[1])

    def goUP(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(),new_y)
    
    def goDOWN(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(),new_y)


