def print_report(resources):
    for key in resources:
        if key in ("water", "milk"):
            print(f"{key.title()}: {resources[key]}ml")
        elif key == "coffee":
            print(f"{key.title()}: {resources[key]}g")
        else:
            print(f"{key.title()}: ${round(resources[key], 2)}")

def are_resources_sufficient(resources, coffee_ingredients_dictionary):
    for ingredient in coffee_ingredients_dictionary:
        if resources[ingredient] < coffee_ingredients_dictionary[ingredient]:
            print(f"Sorry, there is not enough {ingredient}!")
            return False
    return True

def get_number_of_coins(coin):
    while True:
        try:
            number_of_coin = int(input(f"How many {coin} 🪙: "))
            if number_of_coin < 0:
                raise ValueError
            return number_of_coin
        except ValueError:
            print(f"The input for {coin} 🪙 was invalid! Try, again.")

def get_total_coin_sum():
    number_of_quarters = get_number_of_coins("quarters")
    number_of_dimes = get_number_of_coins("dimes")
    number_of_nickels = get_number_of_coins("nickels")
    number_of_pennies = get_number_of_coins("pennies")

    return ((number_of_quarters * 0.25) +
            (number_of_dimes * 0.10) +
            (number_of_nickels * 0.05) +
            (number_of_pennies * 0.01))