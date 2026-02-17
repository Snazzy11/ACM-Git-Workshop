"""
Number Guessing Game is cool
"""

import random

def play_game():
    """Main game loop"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    
    secret_num = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess > secret_num:
                print("Too high! Try a smaller number.")
            elif guess < secret_num:
                print("Too low! Try a bigger number.")
            else:
                print(f"Good job! You guessed it in {attempts} attempts.")
                return True
                
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1

    print(f"Game Over! The number was {secret_num}")
    return False

def get_difficulty():
    """Let player choose difficulty level"""
    # Should return different max_attempts based on difficulty
    # Easy: 15 attempts, Medium: 10 attempts, Hard: 5 attempts
    pass

if __name__ == "__main__":
    play_game()
