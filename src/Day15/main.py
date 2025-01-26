from coffee_machine_data import MENU, resources
from utils import print_report, get_total_coin_sum, are_resources_sufficient

print("Welcome to the Best Coffee Machine!")

should_stop = False

while not should_stop:

    print("What would you like ? Type either 'espresso', 'latte' or 'cappuccino'.")
    coffe_choice = input("Your choice: ").lower()

    if coffe_choice == "off":
        should_stop = True
        continue

    if coffe_choice == "report":
        print_report(resources)
        continue

    while not coffe_choice in ("espresso", "latte", "cappuccino"):
        print("Oops, look's like you made a mistake with your choice! Try, again.")
        print("What would you like ? Type either 'espresso', 'latte' or 'cappuccino'.")
        coffe_choice = input("Your choice: ").lower()

    if resources["water"] == 0:
        should_stop = True
        print("Sorry, look's like the coffee machine has run out of water! It needs to be refilled.")
        continue

    if resources["coffee"] == 0:
        should_stop = True
        print("Sorry, look's like the coffee machine has run out of coffee! It needs to be refilled.")
        continue

    if not are_resources_sufficient(resources, MENU[coffe_choice]["ingredients"]):
        continue

    print("Please, insert coins. 🪙")
    total_sum = get_total_coin_sum()

    coffe_cost = MENU[coffe_choice]["cost"]

    if total_sum < coffe_cost:
        print("Sorry, that is not enough money 💵! Money refunded.")
        continue

    if not "money" in resources:
        resources["money"] = 0
    resources["money"] += coffe_cost

    change = total_sum - coffe_cost
    if change > 0:
        print(f"Here is ${round(change, 2)} dollars 💵 in change.")

    for ingredient in MENU[coffe_choice]["ingredients"]:
        resources[ingredient] -= MENU[coffe_choice]["ingredients"][ingredient]

    print(f"Here is your {coffe_choice} ☕️. Enjoy!")
