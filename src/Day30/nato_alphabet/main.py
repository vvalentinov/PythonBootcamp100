import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

while True:
    word = input("Enter a word: ").upper()
    try:
        if not word:
            raise KeyError
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Oops! Look's like you entered invalid value!")
    else:
        print(output_list)
        break
