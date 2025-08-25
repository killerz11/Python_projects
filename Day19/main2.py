from turtle import Turtle, Screen
import random

def make_turtle(count):
    y_axis = -100
    for i in range(count):
        new_turtle = Turtle("turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_axis)
        all_turtles.append(new_turtle)
        y_axis += 40

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
all_turtles = []
make_turtle(6)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"WON, The winner is {winning_color}")
            else:
                print(f"LOST, The winner is {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()