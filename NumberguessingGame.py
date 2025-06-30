#NUMBER GUESSING GAME
import random

low = 1
high = 100
number = random.randint(low, high)

while True:
        guess = int(input(f"Enter a number between {low} and {high}: "))
        
        if guess < low or guess > high:
            print(f"Please enter a number within the range {low} to {high}.")
            continue

        if guess == number:
            print(f"🎉 Correct Guess! The number was {guess}.")
            break
        elif guess < number:
            print("Too Low! Guess again.")
        else:
            print("Too High! Guess again.")
        print("❗ Please enter a valid integer.")
