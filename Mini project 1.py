import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 10. You have three tries to guess it.")

    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    attempts = 0

    while attempts < 3:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} tries!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if attempts == 3 and guess != secret_number:
        print(f"Sorry, you've used all your tries. The number was {secret_number}.")

# Start the game
guess_the_number()
