print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to treasure island!\n Your mission is to find the treasure")
first_choice = str(input("You're at a cross road, where do you want to go? Type left or right. ")).lower()
trans = 0
door = 0

if first_choice == "left":
    second_choice = str(input("You've come to a lake. There's an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across.  ")).lower()
    if second_choice == "wait":
        third_choice = str(input("What color of door do you wish to open? Type red, yellow or blue. ")).lower()
        if third_choice == "red":
            print("Game Over! This is a door to hell.")
        elif third_choice == "yellow":
            print("Congratulation! You just found yourself a treasure. You win!")
        elif third_choice == "blue":
            print("Game Over! This room is full of angry beast.")
        else:
            print("The door you've chosen does not exist. Game Over!")
    else:
        print("Game Over! The water way is full of deadly pirates.")
else:
     print("Game Over! The path leads to a bottomless pit.")




