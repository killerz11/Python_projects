from turtle import Turtle
import pandas

data = pandas.read_csv("50_states.csv")

class OnMap:
    def __init__(self):
        self.map = Turtle()
        self.map.hideturtle()
        self.map.penup()
        self.map.color("black")

    def write_on_map(self, correct_answer):
        state_data = data[data["state"] == correct_answer]

        x_cor = int(state_data.x.iloc[0])
        y_cor = int(state_data.y.iloc[0])

        self.map.goto(x_cor, y_cor)
        self.map.pendown()
        self.map.write(correct_answer, align="center", font=("Arial", 8, "normal"))
        self.map.penup()
