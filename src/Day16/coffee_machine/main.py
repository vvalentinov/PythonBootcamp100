from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("Welcome to the Best Coffee Machine! ☕️")
should_stop = False
while not should_stop:

    print(f"What would you like ? Type either {menu.get_items()}.")
    coffe_choice = input("Your choice: ").lower()

    if coffe_choice == "off":
        should_stop = True
        continue

    if coffe_choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    menu_item = menu.find_drink(coffe_choice)

    if menu_item is None:
        continue

    if coffee_maker.resources["water"] == 0:
        should_stop = True
        print("Sorry, look's like the coffee machine has run out of water! It needs to be refilled.")
        continue

    if coffee_maker.resources["coffee"] == 0:
        should_stop = True
        print("Sorry, look's like the coffee machine has run out of coffee! It needs to be refilled.")
        continue

    if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
        coffee_maker.make_coffee(menu_item)
