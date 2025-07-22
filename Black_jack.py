import random
import os

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

# Returns a random card from the deck
def deal_card():
    card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_values)

# Calculates the score of a hand
def calculate_score(card_values):
    # Blackjack (Ace + 10)
    if sum(card_values) == 21 and len(card_values) == 2:
        return 0
    # Convert Ace (11) to 1 if score goes over 21
    if 11 in card_values and sum(card_values) > 21:
        card_values.remove(11)
        card_values.append(1)
    # Always return the sum
    return sum(card_values)  # <-- This must be outside the if blocks


def compare(user_score, computer_score):
    if user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score == computer_score:
        return "It's a draw!"
    elif user_score == 0:
        return "Blackjack! You win!"
    elif computer_score == 0:
        return "Computer has Blackjack. You lose!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"
    

print(logo)


# Initialize hands
def play_game():
    user = []
    computer = []
    is_game_over = False

    # Deal 2 cards to both
    for _ in range(2):
        user.append(deal_card())
        computer.append(deal_card())

    # Calculate scores
    while not is_game_over:
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        
        # Print results
        print(f"The user's cards: {user}, score: {user_score}")
        print(f"The computer's cards: {computer}, score: {computer_score}")
        
        
        # End game if someone has blackjack or user goes over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal=input("type 'y' if u want to draw another card and type 'n' if u want to end the game!!")    
            if user_deal=="y":
                user.append(deal_card())
                # user_score=calculate_score(user)
            else:
                is_game_over=True    
    while computer_score!=0 and computer_score<17:
        computer.append(deal_card)
        computer_score=calculate_score(computer)            
        

    print(compare(user_score, computer_score))  


while input(" Do you want to play a game of blackjack? Type 'y' or 'n':")=='y':
    os.system('cls')
    play_game()
 