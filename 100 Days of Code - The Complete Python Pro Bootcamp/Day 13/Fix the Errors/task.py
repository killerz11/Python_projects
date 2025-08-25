try:
    age = int(input("How old are you?"))
except ValueError:
    print("You typed a invalid input, try with numerical number like 12.")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
