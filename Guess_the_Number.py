from random import randint
EASY_LEVEL=10
HARD_LEVEL=5

def check_num(guess,answer,turns):
    if guess> answer:
        print(" this is higher than the correct answer")
        return False
    elif guess< answer:
        print("this is lower than the correct answer")
        return False   
    else :
        print("this is the coorect answer")
        return True

def difficulty():
   level= input("U want the 'easy' or the 'hard ' level ")        
   if level=="easy":
        return EASY_LEVEL
   else:
        return HARD_LEVEL

def game():
    print("wlecome to the number guessing game!")
    print("I\'m  thinking of the number between 1 to 100")
    answer=randint(1,100)
    turns=difficulty()

    while turns>0:
        print(f" you have {turns} attempts remaining ")
        guess =int(input("make a guess"))
        if check_num(guess,answer,turns):
            break
        turns -=1
    else:
        print(f" you have run of guessess . the number was {answer}")
game()



            
 

