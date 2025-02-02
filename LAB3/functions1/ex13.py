import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()  
    
    number = random.randint(1, 20) 
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    attempts = 0
    
    while True:
        guess = int(input("\nTake a guess.\n"))  
        attempts += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"\nGood job, {name}! You guessed my number in {attempts} guesses!")
            break  
guess_the_number()
