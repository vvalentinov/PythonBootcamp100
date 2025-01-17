import random
import data

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
letters_count = int(input("Letters Count: "))
print("How many symbols would you like in your password?")
symbols_count = int(input("Symbols Count: "))
print("How many numbers would you like in your password?")
numbers_count = int(input("Numbers Count: "))

random_password_characters = []
for number in range(0, letters_count):
    random_letter_index = random.randint(0, len(data.letters) - 1)
    random_password_characters.append(data.letters[random_letter_index])
for number in range(0, symbols_count):
    random_symbol_index = random.randint(0, len(data.symbols) - 1)
    random_password_characters.append(data.symbols[random_symbol_index])
for number in range(0, numbers_count):
    random_number_index = random.randint(0, len(data.numbers) - 1)
    random_password_characters.append(data.numbers[random_number_index])

random.shuffle(random_password_characters)
# instead of join function below, we can just use a for loop with concatenation
generated_password = ''.join(random_password_characters)
print(generated_password)
