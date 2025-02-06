import csv

#TODO 1. Create a dictionary in this format:
with open("nato_phonetic_alphabet.csv") as file:
    reader = csv.reader(file)
    next(reader)
    mydict = {rows[0]: rows[1] for rows in reader}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word_input = input("Enter your word here: ").upper()
result = [mydict[character] for character in user_word_input]

print(result)