import random
import data

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
letters_count = int(input("Letters Count: "))
print("How many symbols would you like in your password?")
symbols_count = int(input("Symbols Count: "))
print("How many numbers would you like in your password?")
numbers_count = int(input("Numbers Count: "))

password = ""
for number in range(0, letters_count):
    random_letter_index = random.randint(0, len(data.letters) - 1)
    password += data.letters[random_letter_index]
for number in range(0, symbols_count):
    random_symbol_index = random.randint(0, len(data.symbols) - 1)
    password += data.symbols[random_symbol_index]
for number in range(0, numbers_count):
    random_number_index = random.randint(0, len(data.numbers) - 1)
    password += data.numbers[random_number_index]

print(f"Your generated password is: {password}")
