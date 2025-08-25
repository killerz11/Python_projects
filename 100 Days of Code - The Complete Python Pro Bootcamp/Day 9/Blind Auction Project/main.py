import art

print(art.logo)

def find_highest(bid_dict):
    winner = ""
    highest_bid = 0
    for bid in bid_dict:
       bid_amount = bid_dict[bid]
       if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner = bid
    #alternative way
    #max(bid_dict, key=bid_dict.get)

    print(f"The winner is {winner}")

# TODO-1: Ask the user for input
price_bid = {}
# TODO-2: Save data into dictionary {name: price}

Entry = True
while Entry:
    name = input("Enter the name of the bider  ")
    price = int(input("Enter the bid price  "))
    price_bid[name] = price
    next_bid = input("Is there any other bid?  ").lower()
    if next_bid == "no":
        Entry = False
        find_highest(price_bid)
    elif next_bid == "yes":
        print("\n" * 20)


# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary








