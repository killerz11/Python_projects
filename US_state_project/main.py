import turtle
import pandas
from write_on_map import OnMap

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
onmap = OnMap()

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

correct_guess = 0

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{correct_guess}/50 States correct", prompt="What's another state name ?").title()
    if answer_state =="Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states to learn.csv")
        break
    if answer_state in states:
        correct_guess += 1
        onmap.write_on_map(answer_state)
        guessed_states.append(answer_state)






