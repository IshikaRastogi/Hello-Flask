import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    attempts = 0
    
    print("Welcome! Guess the number between 1 and 20.")
    
    while True:
        user_guess = int(input("Your guess: "))
        attempts += 1
        
        if user_guess == secret_number:
            print(f"Congratulations! Guessed in {attempts} attempts.")
            break
        print("Too low! Try again." if user_guess < secret_number else "Too high! Try again.")

# Run the game
guess_the_number()
