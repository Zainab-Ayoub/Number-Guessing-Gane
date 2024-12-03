import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")

computer_choice = random.randint(0,100)

guess = 0

def easy_level():
    attempts = 10
    print("You have 10 chances!")
    for chance in range(0,10):
        guess = int(input("Guess a Number: "))
        if guess == computer_choice:
            print("You Win!")
            break
        elif guess < computer_choice:
            print("Too Low") 
            attempts -= 1   
            print(f"You have {attempts} attempts left")
        elif guess > computer_choice:
            print("Too High")
            attempts -= 1  
            print(f"You have {attempts} attempts left")
    if attempts == 0:
        print("You lost!")

def hard_level():
    attempts = 5
    print("You have 5 chances!")
    for chance in range(0,5):
        guess = int(input("Guess a Number: "))
        if guess == computer_choice:
            print("You Win!")
            break
        elif guess < computer_choice:
            print("Too Low") 
            attempts -= 1 
            print(f"You have {attempts} attempts left")
        elif guess > computer_choice:
            print("Too High")
            attempts -= 1  
            print(f"You have {attempts} attempts left")
    if attempts == 0:
        print("You lost!")
     



level = input("Select level: 'easy' or 'hard': ")
if level == 'easy':
    easy_level()
elif level == 'hard':
    hard_level()    
