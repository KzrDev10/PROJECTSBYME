from game_data import data
import random
from art import logo,vs
from clear_screen import clear

print(logo)

print("Welcome to the Higher Lower Game! \nTry to guess who has more followers on Instagram")



score = 0
game_should_continue = True
account_b = random.choice(data)






while game_should_continue:
  
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b or account_a["followers"] == account_b["followers"]:
        account_b = random.choice(data)
    
    print(f"Compare A: {account_a["name"]}, {account_a["description"]} , {account_a["followers"]} follwers, {account_a["country"]}")

    print(vs)

    print(f"Against B: {account_b["name"]}, {account_b["description"]}, {account_b["country"]}")


    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    def check_answer(guess, a_followers, b_followers):
        if a_followers > b_followers:
            return guess == "A"
        else:
            return guess == "B"
    a_followers = account_a["followers"]
    b_followers = account_b["followers"]
    iscorrect = check_answer(guess, a_followers, b_followers)

    clear()

    if iscorrect:
        score += 1
        print(f"You're right! Current score: {score}")
        
    else:
        game_should_continue = False
        print(f"Wrong! Final score: {score}")




