import ascii_art
import messages
import random

ascii_art_list = [ascii_art.rock, ascii_art.paper, ascii_art.scissors]

print("Welcome to the famous Rock, Paper, Scissors Game!")
print("Make a Choice! Type 0 for Rock, 1 for Paper or 2 for Scissors.")

choice = int(input("Choice: "))
if choice < 0 or choice >= 3:
    print(messages.invalid_choice_msg)
    exit()
print(ascii_art_list[choice])
computer_choice = random.randint(0, 2)
print("Computer Chose:")
print(ascii_art_list[computer_choice])

if choice == computer_choice:
    print(messages.draw_msg)
elif choice < computer_choice:
    print(messages.you_won_msg if computer_choice - choice == 2 else messages.you_lost_msg)
else:
    print(messages.you_lost_msg if choice - computer_choice == 2 else messages.you_won_msg)
