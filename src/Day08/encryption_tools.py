import data

def shift_letter(alphabet, letter, shift_number):
    index_of_letter = alphabet.index(letter)
    index = (index_of_letter + shift_number) % len(alphabet)  # Handle both directions
    return alphabet[index]

def encrypt(original_text, shift_number):
    encrypted_text = ""
    for letter in original_text:
        if letter in data.alphabet_lower:
            encrypted_text += shift_letter(data.alphabet_lower, letter, shift_number)
        elif letter in data.alphabet_upper:
            encrypted_text += shift_letter(data.alphabet_upper, letter, shift_number)
        else:
            encrypted_text += letter

    return encrypted_text

def decrypt(encrypted_text, shift_number):
    original_text = ""
    for letter in encrypted_text:
        if letter in data.alphabet_lower:
            original_text += shift_letter(data.alphabet_lower, letter, -shift_number)
        elif letter in data.alphabet_upper:
            original_text += shift_letter(data.alphabet_upper, letter, -shift_number)
        else:
            original_text += letter

    return original_text