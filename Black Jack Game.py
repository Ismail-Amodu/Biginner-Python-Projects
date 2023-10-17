import random

#Return a random card from the deck.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    
#Deal the user and computer 2 cards each using deal_cards()
user_cards = []
computer_cards = []
is_game_over = False

while not is_game_over:
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #Creating a function that takes a list of cards as input
    #and returns the score.
    def calculate_score(cards):
        #Inside the calculate_score() check for a blackjack (a hand with only 2 cards: ace +10)
        #and retun 0 instead of the actual score. ) will represent a blackjack in our game
        #if 11 in cards and 10 in cards and len(cards) == 2:
        if sum(cards) == 21 and len(cards) == 21:
            return 0
        
        #Inside calcuator-score() check for an 11 (ace). If the score is already over 21,
        #remove the 11 and replace by a 1. append() and remove() bult-in function is used.
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return calculate_score(cards)

    #call calculate_score(). If the computer or the user has a blackjack (0) or if the
    #user's score is over 21, then the game ends
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
        
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over == True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
