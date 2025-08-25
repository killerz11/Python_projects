from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.new_xaxis = 10
        self.new_yaxis = 10
        self.move_speed = 0.1


    def move(self):
        x_axis = self.xcor() + self.new_xaxis
        y_axis = self.ycor() + self.new_yaxis
        self.goto(x_axis, y_axis)

    def bounce_y(self):
        self.new_yaxis *= -1

    def bounce_x(self):
        self.new_xaxis *= -1
        if self.move_speed >= 0.02:
            self.move_speed *= 0.95

    def reset_pos(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
