# text = "thIS is mY TexT"
# print(text.title())

def format_name(f_name, l_name):
    """Take a first and last name and return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs!"

    first_name = f_name.title()
    last_name = l_name.title()

    return f"{first_name} {last_name}"

print(format_name(input("What is your first name: "), input("What is your last name: ")))