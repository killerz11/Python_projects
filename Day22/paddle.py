from turtle import Turtle

SPEED = 40

class Paddle(Turtle):
    def __init__(self,start_pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(start_pos)

    def go_up(self):
            new_y = self.ycor() + SPEED
            self.goto(self.xcor(), new_y)

    def go_down(self):
            new_y = self.ycor() - SPEED
            self.goto(self.xcor(), new_y)