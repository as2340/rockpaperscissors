rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

# create list of ascii art stings
rock_paper_scissors = [rock, paper, scissors]

# use input is the index of the list of ascii strings
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
# print out user's ascii art
print(rock_paper_scissors[user_choice])

# select random integer for computer's choice
computer_choice = random.randint(0,2)
print("Computer chose:")
print(rock_paper_scissors[computer_choice])

# logic to determine winner
if user_choice == computer_choice:
    print("Draw")
elif user_choice == 0: # rock
    if computer_choice == 1: # paper
        print("You lose")
    else:
        print("You win!")
elif user_choice == 1: # paper
    if computer_choice == 2: # scissors
        print("You lose")
    else:
        print("You win!")
else: # user choice is 2 - scissors
    if computer_choice == 0: # rock
        print("You lose")
    else:
        print("You win!")
