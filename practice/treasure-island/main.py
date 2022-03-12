print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


#User input choice
choice1 = input("You are at the middle of cross road. Where do you want to go? Type 'left' or 'right' \n").lower()

if choice1 == "left":
  print("You have selected left")
  choice2 = input("You found a lake! Do you want to swim or wait for the boat? Type 'swim' or 'wait' \n").lower()
  
  if choice2 == "wait":
    choice3 = input("You arrive safely on another island and you found a house with 3 doors red, blue and yellow. Which door do you want to go in? Type 'red' 'blue' or 'yellow' \n").lower()

    if choice3 == "red":
      print("You have selected red door")
      print("Game over you were burned by the fire!")

    elif choice3 == "yellow":
      print("You have selected yellow door")
      print("You win hooray you found the treasure!")

    elif choice3 == "blue":
      print("You have selected blue door")
      print("Game over you were eaten by the beast!")

    else:
      print(f"You have selected {choice3} ")
      print("Game over the door you select not exist")

  else:
    print("You hsave selected swim")
    print("Game over you attack by trout in the lake")

else:
  print("You have selected right")
  print("Game over you fall into a hole.")