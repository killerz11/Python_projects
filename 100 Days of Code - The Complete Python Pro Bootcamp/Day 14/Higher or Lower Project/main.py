
from game_data import data
from art import logo, vs
import random



def format_competitor(competitor):
    """take the followers acc and return Formatted data into printable format"""
    comp_name = competitor['name']
    comp_description = competitor['description']
    comp_country = competitor['country']

    return f"{comp_name}, {comp_description}, {comp_country}"

def check_answer(guess, a_followers, b_followers):
    """take the followers acc and return who is right"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
b_competitor = random.choice(data)
game_on = True
while game_on:

    #Display art
    print(logo)

    #generate acc from dictionary
    a_competitor = b_competitor
    b_competitor = random.choice(data)
    if a_competitor == b_competitor:
        b_competitor = random.choice(data)

    print(f"Compare A: {format_competitor(a_competitor)}")
    print(vs)
    print(f"Against B: {format_competitor(b_competitor)}")

    a_follower = a_competitor['follower_count']
    b_follower = b_competitor['follower_count']

    answer = input("Who has more followers 'A' or 'B' ").lower()
    print("\n" * 20)
    print(logo)
    is_correct = check_answer(answer, a_follower, b_follower)

    if is_correct:
        score += 1
        print(f"You're right, current score is {score} ")
    else:
        print(f"sorry! you're wrong, final score is {score} ")
        game_on = False







