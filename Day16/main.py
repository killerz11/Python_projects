# from turtle import Turtle,  Screen
#
# jack = Turtle()
# print(jack)
# jack.shape("turtle")
# jack.color("cyan")
# jack.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle",  "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)