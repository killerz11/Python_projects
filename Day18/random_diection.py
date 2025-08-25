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
jacky.pensize(9)
jacky.speed(10)

direction = [90,180,270,0]

for _ in range(200):
    jacky.color(randomcolor())
    jacky.forward(30)
    jacky.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()