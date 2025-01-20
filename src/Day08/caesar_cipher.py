import art
import data
import encryption_tools

print("Welcome to the Caesar Cipher!")
print(art.logo)

continue_with_game = True

while continue_with_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    while direction not in ("encode", "decode"):
        print("Oops! Seems like you made a mistake!")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    text = input("Type your message: ")

    shift = 0
    while True:
        try:
            shift = int(input("Type the shift number: ")) % len(data.alphabet_lower)
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    result_text = ""
    if direction == "encode":
        result_text = encryption_tools.encrypt(text, shift)
    else:
        result_text = encryption_tools.decrypt(text, shift)

    print(f"Your result is: {result_text}")
    continue_with_game = input("Would you like to continue? Type 'yes' or 'no': ").lower() == "yes"

print("Goodbye! See you next time.")
