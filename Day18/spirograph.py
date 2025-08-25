import turtle
from turtle import Turtle, Screen
import random

jacky = Turtle()
turtle.colormode(255)

def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

jacky.shape("turtle")
jacky.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        jacky.color(randomcolor())
        jacky.circle(150)
        jacky.setheading(jacky.heading() + size_of_gap)

draw_spirograph(1)

screen = Screen()
screen.exitonclick()





