import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")

computer_choice = random.randint(0,100)

guess = 0

def easy_level():
    print("You have 10 chances!")
    for chance in range(0,10):
        guess = int(input("Guess a Number: "))
        if guess == computer_choice:
            print("You Win!")
            break
        elif guess < computer_choice:
            print("Too Low")    
        elif guess > computer_choice:
            print("Too High")

     



level = input("Select level: 'easy' or 'hard': ")
if level == 'easy':
    easy_level()
# elif level == 'hard':
#     hard_level()    
