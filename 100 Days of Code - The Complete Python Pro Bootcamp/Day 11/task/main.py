import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, comp_score):
    if u_score == comp_score:
        return "DRAW "
    elif comp_score == 0:
        return "Lose, opponent has a blackjack"
    elif u_score == 0:
        return  "Win with a blackjack"
    elif u_score > 21:
        return "You went over 21, You Lose"
    elif comp_score > 21:
        return "Opponent went over, you win"
    elif u_score > comp_score:
        return "You win"
    else:
        return "You Lose"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computers first hand: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_over = True
        else:
            user_deal = input("Type 'y' to draw another card and 'n' to pass ").lower()
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} and final score is {user_score}")
    print(f"Computer's final hand: {computer_cards} and final score is {computer_score}")
    print(compare(user_score, computer_score))

while input("DO YOU WANNA PLAY A GAME OF BLACKJACK 'y' or 'n' ").lower() == "y":
    print("\n *  n")
    play_game()

