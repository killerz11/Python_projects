import turtle
from turtle import Turtle, Screen
import random
#import turtle as t
jacky = Turtle()
jacky.shape("turtle")
jacky.color("coral")

colors = ["red", "blue", "green", "yellow", "black", "orange", "purple", "pink", "brown",
          "gray", "cyan", "magenta", "lime", "maroon", "navy", "teal", "olive", "gold", "silver"]


for i in range(3, 11):
    angle = 360/i
    for _ in range(i):
        jacky.color(random.choice(colors))
        jacky.forward(100)
        jacky.right(angle)





















screen = Screen()
screen.exitonclick()