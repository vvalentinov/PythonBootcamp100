import art

print("Welcome to the Secret Auction Program!")
print(art.logo)

bidders_dictionary = {}
continue_with_bid = "yes"

while continue_with_bid == "yes":
    # Get the bidder's name
    name = input("What is your name: ")
    while name in bidders_dictionary:
        print("Oops! This name is currently taken. Maybe try a different alias.")
        name = input("What is your name: ")

    # Get the bidder's bid
    while True:
        try:
            bid_price = int(input("What is your bid: "))
            if bid_price <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Oops!  That was no valid number for a bid.  Try again...")

    # Add the bidder with his bid
    bidders_dictionary[name] = bid_price
    # Check if to continue with the bidding process
    continue_with_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    while continue_with_bid not in ("yes", "no"):
        print("Oops! Seems like you made a mistake with your spelling. Try again, please.")
        continue_with_bid = input("Are there more people to bid? Type 'yes' or 'no': ")
    # If the bidding continues - print 50 empty lines
    if continue_with_bid == "yes":
        print("\n" * 50)

# Option 1
max_bid = 0
winner_name = ""

for key in bidders_dictionary:
    current_bid = bidders_dictionary[key]
    if current_bid > max_bid:
        winner_name = key
        max_bid = current_bid

print(f"The winner is {winner_name} with a bid of ${max_bid} dollars. Congratulations!")

# Option 2
# key = max(bidders_dictionary, key=bidders_dictionary.get)
# print(f"The winner is {key} with a bid of ${bidders_dictionary[key]} dollars. Congratulations!")
