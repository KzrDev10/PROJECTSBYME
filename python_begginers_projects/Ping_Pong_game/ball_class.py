from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
          super().__init__()
          self.shape("circle")
          self.color("white")
          self.penup()
          self.shapesize(stretch_len=1,stretch_wid=1)
          self.goto(x=0,y=0)
          self.x_move = 10
          self.y_move = 10

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move

        self.goto(x=new_x,y=new_y)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
    
    def refresh(self):
        self.goto(x=0,y=0)
    