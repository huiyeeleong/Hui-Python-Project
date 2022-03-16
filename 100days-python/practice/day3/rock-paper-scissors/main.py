#module
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
icon = [rock, paper, scissors]

#user selection
user_option = input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for scissors \n")
user_option = int(user_option)

#print out the icon
print(icon[user_option])

#computer selection with randomnize
print(" ")
computer_option = random.randint(0, 2)
computer_icon = icon[computer_option]

print(f"Its now computer turn, Computer will choose")
print(computer_icon)


if user_option >= 3 or user_option < 0: 
  print("You typed an invalid number, you lose!")

elif user_option > computer_option:
  print("You won")

elif user_option < computer_option:
  print("You lost")

elif user_option == computer_option:
  print("Its a draw") 

elif user_option == 0 and computer_option == 2:
  print("You win!")
elif computer_option == 0 and user_option == 2:
  print("You lose")

