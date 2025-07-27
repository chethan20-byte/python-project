from game_data import data
import random

# Function to format account info (without follower count)
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Function to check answer
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Game Start
score = 0
repeat_game = True
account_b = random.choice(data)

print("""
  _    _ _       _               _                    _         
 | |  | (_)     | |             | |                  | |        
 | |__| |_  __ _| |__   ___ _ __| |     ___  __ _  __| | ___    
 |  __  | |/ _` | '_ \ / _ \ '__| |    / _ \/ _` |/ _` |/ _ \   
 | |  | | | (_| | | | |  __/ |  | |___|  __/ (_| | (_| | (_) |  
 |_|  |_|_|\__, |_| |_|\___|_|   \_____/\___|\__,_|\__,_|\___/   
             __/ |                                                
            |___/                                                 
""")

while repeat_game:
    account_a = account_b
    account_b = random.choice(data)
    
    # Ensure they are not the same
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print("""
    __      _______ 
    \ \    / / ____|
     \ \  / / (___  
      \ \/ / \___ \ 
       \  /  ____) |
        \/  |_____/ 
    """)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"\n✅ Yay!! You are correct. Your current score is: {score}\n")
    else:
        repeat_game = False
        print(f"\n❌ Oh no! You are wrong. Your final score is: {score}\n")
