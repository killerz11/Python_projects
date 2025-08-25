print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

Total_amt = bill + (bill*tip/100)
Final_amt = Total_amt/people

print(f"Each person has to pay = {round(Final_amt,2)}")
