import random
# import random

def deal_card():
    card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_values)

user = []
computer = []

for _ in range(2):
    user.append(deal_card())
    computer.append(deal_card())

print("User cards:", user)
print("Computer cards:", computer)
