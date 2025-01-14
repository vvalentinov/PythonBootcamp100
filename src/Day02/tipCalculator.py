print("Welcome to the Tip Calculator!")
print("What was the total $bill?")
bill = float(input("Total: $"))
print("What percentage tip would you like to give? Choose either 10, 12 or 15.")
tip = int(input("Tip: %")) / 100
print("How many people to split the bill?")
people = int(input("People: "))
result = round((bill + (bill * tip)) / people, 2)
print(f"Each person should pay: ${result}!")
