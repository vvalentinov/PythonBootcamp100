import random
import hangman_art
import hangman_words

print("Welcome to the famous Hangman Game!")
print(hangman_art.logo)

random_word = random.choice(hangman_words.word_list)
print("_" * len(random_word))

lives = len(hangman_art.stages) - 1

display_word = ["_"] * len(random_word)
guessed_letters = []

while "_" in display_word and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'! For that reason I won't take a life away from you. Try something else.")
        continue
    guessed_letters.append(guess)

    if guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == guess:
                display_word[i] = guess
        print(f"Yes! You chose {guess}, which is correct! You get to keep your lives for now.")
    else:
        lives -= 1
        print(f"Oops! You chose {guess}, but that is wrong! You loose a life.")

    print(hangman_art.stages[lives])
    print(f"Current Word State: {''.join(display_word)}")
    print(f"Remaining Lives: {lives}")

if lives == 0:
    print("Game Over! You lost all of your lives! Should have used them wisely.")
    print(f"The word was: {random_word}. Pretty cool, huh?")
else:
    print(f"You Won, Congratulations! You guessed the word {random_word} correctly.")
