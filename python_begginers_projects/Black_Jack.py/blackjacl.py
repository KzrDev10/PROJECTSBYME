import random
from clear import clear

def deal_card():
    '''Returns a random card from the deck.'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer has a BlackJack, You lose"
    elif user_score == 0:
        return "You have a BlackJack, You win"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Computer went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    
    gameOver = False

    user_card= []
    computer_card = []

    # underscore is used to ignore the variable
    #when you dont care about it
    #you just wanna loop
    
    for _ in range(2):    
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not gameOver:
        print(f"Your cards: {user_card}, current score: {calculate_score(user_card)}")   
        print(f"Computer's first card: {computer_card[0]}")

        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            gameOver = True
        else:
            user_input= input("You wanna draw another card y for yes and n for no: ")
        if user_input == 'y':
            user_card.append(deal_card())
        else:
            gameOver = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no: ") == 'y':
    clear()
    play_game()