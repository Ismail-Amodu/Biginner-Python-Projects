
#Number Guessing Game
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of number between 1 and 100")
EAZY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Function to set difficulty level
def set_difficulty():
    difficulty_level = input("Choose difficulty level. Type 'easy' or 'hard': ") 
    if difficulty_level == "easy":
        return EAZY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
#Function to check answers and return number of attempt remaining
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high!")
        return turns -1
    elif guess < answer:
        print("Too low!")
        return turns -1
    else:
        print("You win!")

def game():
    turns = set_difficulty()
    
    answer = random.randint(1, 100)
        
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: ")) 
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("You've run out of guesses. You lose!")
            return
        elif guess != answer:
            print("Guess again!")
game()

        