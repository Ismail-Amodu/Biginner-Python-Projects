#Rock, Paper and Scissors game
import random
print("This is Rock, Paper and Scissors game")
rock = '''    
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''    
---'    ____)____
           ______)
          _______)
         _______)
---.__________'''

scissors = '''   
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

your_choice = int(input("what do you choose? Type 0 for rock, 1 for paper, and 2 for scissors: "))
 
if your_choice == 0:
    print(f"{rock}\nYou chose a rock.")
elif your_choice == 1:
    print(f"{paper}\nYou chose a paper.")
elif your_choice == 2:
    print(f"{scissors}\nYou chose a scissors.")
else:
    print("Game Over! You typed something outside 0, 1, or 2.")

computer_choice = random.randint(0,2)
random.seed(computer_choice)
computer_image = random.randint(0,2)

if computer_image == 0:
    print(f"{rock}\nComputer chose a rock.")
elif computer_image == 1:
    print(f"{paper}\nComputer chose a paper.")
else:
    print(f"{scissors}\nComputer chose a scissors.")
   
if (your_choice == 0 and computer_choice == 1):
    print("You Lose")
elif  (your_choice == 0 and computer_choice == 2):
    print("You Win!")
elif (your_choice == 1 and computer_choice == 0):
    print("You Win")
elif  (your_choice == 1 and computer_choice == 2):
    print("You Lose!")
elif (your_choice == 2 and computer_choice == 0):
    print("You Lose")
elif  (your_choice == 2 and computer_choice == 1):
    print("You Win!")
else:
    print("A draw!")


