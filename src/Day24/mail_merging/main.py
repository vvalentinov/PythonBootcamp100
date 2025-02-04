with open("./Input/Names/invited_names.txt") as file:
    for line in file:
        name = line.rstrip()

        with open("./Input/Letters/starting_letter.txt") as f:
            lines = f.readlines()

        # Option One:
        # lines[0] = f"Dear {name},\n"

        # Option Two:
        lines[0] = lines[0].replace("[name]", name)

        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
            f.writelines(lines)