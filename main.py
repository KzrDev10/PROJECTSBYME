from art import logo
from clear_screen import clear

print(logo)

bid_finished = False
bid_value = {}

def find_highest_bidder(bidding_record):
    highest = 0
    winner = ""
    for bidder,amount in bidding_record.items():
        amount > highest
        highest = amount
        winner = bidder
    print(f"\nThe winner of the auction is {winner} with a bid of ${highest}")


while not bid_finished:
    name = input("What is your name: ")
    bid = int(input("Whats is your bid: $"))

    bid_value[name] = bid #key is name and value is bid
    repeat = input("Are there any other bidders type Yes or No: ").lower()
    if repeat == "no":
        bid_finished = True
        find_highest_bidder(bid_value) # this makes bid_value = bidding_record in the function
    elif repeat == "yes":
        clear()
    




