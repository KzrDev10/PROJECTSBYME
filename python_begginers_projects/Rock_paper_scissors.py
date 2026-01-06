import  random

print("Welcome to Rock Paper Scissors Game !")



user_choice = int(input("What do you choose? Type 0 for rock 1 for paper and 2 for scissors: "))


rock = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

a_choices = [rock,scissors,paper]
user_choice = a_choices[user_choice]
computers_choice = random.choice(a_choices)




print(f'Computer chose:\n {computers_choice} \n You chose:\n {user_choice}')
if  user_choice == computers_choice:
    print("It's a draw")
elif (user_choice == rock and computers_choice == scissors) or (user_choice == scissors and computers_choice == paper) or (user_choice == paper and computers_choice == rock):
    print("You win!")
elif (computers_choice == rock and user_choice == scissors) or (computers_choice == scissors and user_choice == paper) or (computers_choice == paper and user_choice == rock):
    print("You lose")
else:
    print("Invalid input! You lose")

play_again = input("Do you wanna play again press y for yes and n for no").lower()
    
#add  loop for replaying the game