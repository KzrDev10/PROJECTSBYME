from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle): #inheritance
    def __init__(self):
        super().__init__() #this used to inherit turtles attribtes and method
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0,y=260)
        self.score = 0
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT, font=FONT)

    def gameOver(self):
        self.penup()
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)
        self.goto(0,-24)
        
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    
    def endnote(self):
        self.write(f"Your score is {self.score}",align=ALIGNMENT,font=FONT)
