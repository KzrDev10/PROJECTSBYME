print("Welcome to Chun Chun pizza deliveries")
size = input("What size do you want? S,M,L: ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0

if size =="S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y" and size == "S":
    bill +=2
elif add_pepperoni == "Y" and (size == "M" or "L"):
    bill += 3

if extra_cheese == "Y":
    bill += 1


print(f'Your final bill is: ₦{bill}')