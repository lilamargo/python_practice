import random

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

game_images = [rock, paper, scissors]

user_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("\nComputer chose:\n")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("\n You typed an invalid number, you lose!\n") 
elif user_choice == 0 and computer_choice == 2:
  print("\nYou win!\n")
elif computer_choice == 0 and user_choice == 2:
  print("\nYou lose!! :(\n")
elif computer_choice > user_choice:
  print("\nYou lose!! :(\n")
elif user_choice > computer_choice:
  print("\nYou win!! :)\n")
elif computer_choice == user_choice:
  print("\nIt's a draw!!\n")