from random import randint
import art

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#            31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
#            61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
#            91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

#Chosen_num = random.choice(numbers)
Chosen_num = randint(1,100)

def difficulty():
    choice = input("Choose the difficulty easy or hard : ").lower()
    if choice == "easy":
        attempt = 10
    else:
        attempt = 5
    print(f"you have got {attempt} attempts")
    return attempt

print(art.logo)
print("Thinking of number between 1 and 100")
attempts = difficulty()
game_on = True

while game_on:

    if attempts == 0:
        print("You finished all your attempts")
        game_on = False

    else:
        guessed_num = int(input("Guess the number "))
        if guessed_num == Chosen_num:
            print("You guessed the right number ")
            game_on = False
        elif guessed_num > Chosen_num:
            print("Too high ")
        else:
            print("Too low ")
        attempts -= 1
