MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report():
    available_water = resources['water']
    available_milk = resources['milk']
    available_coffee = resources['coffee']
    print(f"Available water:{available_water}\nAvailable milk:{available_milk}\nAvailable coffee:{available_coffee}")

def check_input(user_entry):
    if user_entry == 'report':
        print_report()

#TODO 2: check for sufficient resources

def check_resources(user_entry):
    available_water = resources['water']
    available_milk = resources['milk']
    available_coffee = resources['coffee']

    espresso_water = MENU['espresso']['ingredients']['water']
    espresso_coffee = MENU['espresso']['ingredients']['coffee']

    latte_water = MENU['latte']['ingredients']['water']
    latte_coffee = MENU['latte']['ingredients']['coffee']
    latte_milk = MENU['latte']['ingredients']['milk']

    cappuccino_water = MENU['cappuccino']['ingredients']['water']
    cappuccino_coffee = MENU['cappuccino']['ingredients']['coffee']
    cappuccino_milk = MENU['cappuccino']['ingredients']['milk']

    if user_entry == 'espresso':
        if available_water >= espresso_water and available_coffee >= espresso_coffee:
            return True
        else:
            print("Sorry! there are not sufficient resources")
    elif user_entry == 'latte':
        if available_water >= latte_water and  available_coffee >= latte_coffee and available_milk >= latte_milk:
            return True
        else:
            print("Sorry! there are not sufficient resources")
    elif user_entry == 'cappuccino':
        if available_water >= cappuccino_water and  available_coffee >= cappuccino_coffee and available_milk >= cappuccino_milk:
            return True
        else:
            print("Sorry! there are not sufficient resources")


#TODO 3: check the money of the user

def check_money(user_entry, money):

    espresso_price = MENU['espresso']['cost']
    latte_price = MENU['latte']['cost']
    cappuccino_price = MENU['cappuccino']['cost']

    print("How much money do you have ?\n")
    user_quarters = int(input("Quarters : "))
    user_dimes = int(input("Dimes : "))
    user_nickles = int(input("Nickles : "))
    user_pennies = int(input("Pennies : "))

    total_amt = user_quarters * 0.25 + user_dimes * 0.10 + user_nickles * 0.05 + user_pennies * 0.01

    if user_entry == 'espresso':
        if total_amt >= espresso_price:
            money += espresso_price
            if total_amt != espresso_price:
                refund = total_amt - espresso_price
                print(f"Here's your change {refund}")
                return money, True

#TODO 4: deduct resources
def deduct_resources(user_entry):
    available_water = resources['water']
    available_milk = resources['milk']
    available_coffee = resources['coffee']

    espresso_water = MENU['espresso']['ingredients']['water']
    espresso_coffee = MENU['espresso']['ingredients']['coffee']

    latte_water = MENU['latte']['ingredients']['water']
    latte_coffee = MENU['latte']['ingredients']['coffee']
    latte_milk = MENU['latte']['ingredients']['milk']

    cappuccino_water = MENU['cappuccino']['ingredients']['water']
    cappuccino_coffee = MENU['cappuccino']['ingredients']['coffee']
    cappuccino_milk = MENU['cappuccino']['ingredients']['milk']

    if user_entry == 'espresso':
        available_water -= espresso_water
        available_coffee -= espresso_coffee


#TODO 1: Prompt user to take input
profit = 0
user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
check_input(user_input)
if check_resources(user_input):
    if check_money(user_input, profit):
        profit = check_money(user_input, profit)







