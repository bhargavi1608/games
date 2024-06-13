import random

def guessing_game():
    random_value = random.randint(1, 50)
    guess = None
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 50. Can you guess what it is?")

    while guess != random_value:
        try:
            guess = int(input("Enter a value between 1 and 50: "))
            if guess < 1 or guess > 50:
                print("Please enter a number within the range of 1 to 50.")
                continue

            if guess > random_value:
                print("Too high, please select a lower value.")
            elif guess < random_value:
                print("Too low, please select a higher value.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print(f"Congratulations! You've guessed the correct number: {random_value}")

guessing_game()
