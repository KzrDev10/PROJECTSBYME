import random
import word_list_for_hangman
from hangman_art import stages,logo
# or from word_list_for_hangman import word_list




lives = 6


display = []

chosen_word = random.choice(word_list_for_hangman.word_list)

for blank in chosen_word:
    display += "_"

end_of_game = False 
print(logo)
while not end_of_game:
    print("Welcome to Hangmnan!")


    user_guess = input("Guess a letter!: ").lower()
        

    for guess in range(len(chosen_word)):
        letter = chosen_word[guess]
        if letter == user_guess:    
            display[guess] = letter
        if letter not in chosen_word:
            print("Letter not in word.")
    
    if user_guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(chosen_word)
    

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print (stages[lives])

