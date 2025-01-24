import art
import random

print("Welcome to the Number Guessing Game!")
print(art.logo)

number = random.randint(1, 100)
guesses = 0

print("I have thought of a number between 1 and 100. Your job is to try and guess it.")
print("Pick an easy or hard mode. Easy mode gets you 5 guesses and hard mode gets you 10 guesses.")
level_choice = input("Type 'easy' or 'hard': ").lower()
while not level_choice in ("easy", "hard"):
    print("Oops! Looks like you made a spelling error! Try again.")
    level_choice = input("Pick an easy or hard mode. Just type 'easy' or 'hard': ")

guesses = 10 if level_choice == "easy" else 5
while guesses > 0:

    while True:
        try:
            guess = int(input("What is your guess: "))
            break
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")

    if guess == number:
        print("You guessed correctly! Congratulations!")
        print(art.won_art)
        break

    guesses -= 1
    if guesses == 0:
        print("You ran out of guesses! Sorry!")
        print(f"The number was: {number}.")
        print(art.lost_art)
        break

    if guess < number:
        print("Too low. Try again!")
    else:
        print("Too high. Try again!")

    print(f"You have {guesses} guesses remaining!")
