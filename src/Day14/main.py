import random
from art import logo, vs
from game_data import data

print("Welcome to the Higher Or Lower Game!")
print(logo)

score = 0
game_over = False
first_account = random.choice(data)

while not game_over:
    second_account = random.choice(data)
    while second_account == first_account:
        second_account = random.choice(data)

    print(f"Compare A: {first_account["name"]}, {first_account["description"]} from {first_account["country"]}.")
    print(vs)
    print(f"Compare B: {second_account["name"]}, {second_account["description"]} from {second_account["country"]}.")

    choice = input("Who has more followers? Type either 'A' or 'B': ").lower()
    while not choice in ("a", "b"):
        print("Look's like you made a mistake with your spelling! Try, again.")
        choice = input("Who has more followers? Type either 'A' or 'B': ").lower()

    if choice == "a" and first_account["follower_count"] < second_account["follower_count"]:
        game_over = True
    elif choice == "b" and first_account["follower_count"] > second_account["follower_count"]:
        game_over = True

    if not game_over:
        score += 1
        print("\n" * 20)
        print(f"You are right! Current score: {score}.")

    first_account = second_account

print(f"Game Over! Your score is: {score}.")
