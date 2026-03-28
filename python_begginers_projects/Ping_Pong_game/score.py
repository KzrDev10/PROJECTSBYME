from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self,name,position):
        super().__init__()
        self.score = 0
        self.name = name
        self.color("white")
        self.penup()
        self.hideturtle()
        self.position = ()
        self.goto(x=position[0],y=position[1])
        self.update_score()
        
    def update_score(self):
        self.write(f"{self.name}: {self.score}",align=ALIGNMENT,font=FONT)
     
    def get_point(self):
        self.score +=1
        self.clear()
        self.update_score()
        
