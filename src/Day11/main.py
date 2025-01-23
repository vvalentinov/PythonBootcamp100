import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to the Blackjack Project!")
print(art.logo)

def deal_card(score):
    card = random.choice(cards)
    if card == 11 and score + card > 21:
        card = 1
    return card

player_cards = [random.choice(cards), random.choice(cards)]
player_score = player_cards[0] + player_cards[1]
dealer_cards = [random.choice(cards)]
dealer_score = dealer_cards[0]
game_over = False

print(f"Your Cards: {player_cards}. Current Score: {player_score}")
print(f"Computer First Card: {dealer_cards[0]}")

if player_score < 21:
    want_another_card = input("Type 'yes' to get another card or 'no': ").lower() == "yes"
    while want_another_card:
        random_card = deal_card(player_score)
        player_cards.append(random_card)
        player_score += random_card
        print(f"Your Cards: {player_cards}. Current Score: {player_score}")
        if player_score == 21:
            break
        if player_score > 21:
            game_over = True
            break
        want_another_card = input("Type 'yes' to get another card or 'no': ").lower() == "yes"

if not game_over:
    random_card = deal_card(dealer_score)
    dealer_cards.append(random_card)
    dealer_score += random_card
    while dealer_score < player_score:
        random_card = deal_card(dealer_score)
        dealer_cards.append(random_card)
        dealer_score += random_card
        if dealer_score >= 21:
            break

if player_score == dealer_score:
    print("Draw 🙃")
elif player_score < dealer_score == 21:
    print("Lose, opponent has Blackjack 😱")
elif player_score == 21 and player_score > dealer_score:
    print("Win with a Blackjack 😎")
elif player_score > 21:
    print("You went over. You lose 😭")
elif dealer_score > 21:
    print("Opponent went over. You win 😁")
elif player_score > dealer_score:
    print("You win 😃")
else:
    print("You lose 😤")

print(f"Player Cards: {player_cards}. Score: {player_score}")
print(f"Dealer Cards: {dealer_cards}. Score: {dealer_score}")