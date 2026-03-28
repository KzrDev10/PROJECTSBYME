from turtle import Turtle
FONT = ("Courier",24,"normal")

class Score(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def gameover(self):
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=0)
        self.write("GAMEOVER",24,align="center",font=FONT)

    def Levels(self):
        self.hideturtle()
        self.goto(x=-250,y=260)
        self.penup()
        self.write(f"Level: {self.level}",align="left",font=FONT) #note after posting add the levels thingy so taht the person is aware of the current level they are w.r.t the car speed

    def Levelled_up(self):
        self.clear()
        self.level+=1
        self.write(f"Level: {self.level}",align="left",font=FONT)