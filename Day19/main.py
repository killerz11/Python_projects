import turtle
from turtle import Turtle, Screen

jacky = Turtle()
screen = Screen()

def move_forwards():
    jacky.forward(15)

def move_backwards():
    jacky.backward(15)

def move_right():
    jacky.right(10)

def move_left():
    jacky.left(10)

def clear_screen():
    jacky.clear()
    jacky.penup()
    jacky.home()
screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "a", fun = move_right)
screen.onkey(key = "d", fun = move_left)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "c", fun=clear_screen)

screen.exitonclick()
