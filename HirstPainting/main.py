# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('Hirstspotpainting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
jacky = Turtle()
jacky.hideturtle()
color_list = [(144, 76, 50), (188, 165, 117), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]
jacky.penup()
jacky.setheading(225)
jacky.forward(250)
jacky.setheading(0)
jacky.speed("fastest")
no_of_dots = 100

for dot_count in range(1, no_of_dots + 1):
    jacky.dot(15, random.choice(color_list))
    jacky.forward(50)

    if dot_count % 10 == 0:
        jacky.setheading(90)
        jacky.forward(50)
        jacky.setheading(180)
        jacky.forward(500)
        jacky.setheading(0)



screen = Screen()
screen.exitonclick()