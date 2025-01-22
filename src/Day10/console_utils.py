def get_number_input(message):
    """
        Prompts the user to enter a valid number (integer or float) using the given message.
        Repeats until valid input is provided, converting whole numbers to integers.

        Args:
            message (str): The prompt message.

        Returns:
            int or float: The user's input as an integer or float.
    """
    while True:
        try:
            number = float(input(message))
            if number.is_integer():
                number = int(number)
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    return number

def get_operator_input():
    """
        Prompts the user to enter a valid mathematical operator ('+', '-', '*', or '/').
        Repeats until a valid operator is provided.

        Returns:
            str: The valid operator entered by the user.
    """
    operator = input("What is the operator? Type either '+', '-', '*' or '/': ")
    while not operator in ("*", "/", "+", "-"):
        print("Oops!  That was no valid operator.  Try again...")
        operator = input("What is the operator? Type either '+', '-', '*' or '/': ")
    return operator

def get_exit_program_input():
    """
        Prompts the user to confirm whether they want to exit the program by typing 'yes' or 'no'.
        Repeats until a valid input is provided.

        Returns:
            bool: True if the user enters 'yes', False if the user enters 'no'.
    """
    exit_program = input("Do you want to exit the program? Type either 'yes' or 'no': ").lower()
    while exit_program not in ("yes", "no"):
        print("Oops looks like you made a mistake with your spelling. Try, again.")
        exit_program = input("Do you want to exit the program? Type either 'yes' or 'no': ").lower()
    return exit_program == "yes"

def get_continue_with_prev_result_input(result):
    """
        Asks the user whether to continue with a previous result, displaying the result in the prompt.
        Repeats until a valid input ('yes' or 'no') is provided.

        Args:
            result: The previous result to be shown in the prompt.

        Returns:
            bool: True if the user enters 'yes', False if the user enters 'no'.
    """
    continue_with_prev_result = input(f"Do you want to continue with the previous result ({result})? Type either 'yes' or 'no': ").lower()
    while continue_with_prev_result not in ("yes", "no"):
        print("Oops looks like you made a mistake with your spelling. Try, again.")
        continue_with_prev_result = input(f"Do you want to continue with the previous result ({result})? Type either 'yes' or 'no': ").lower()
    return  continue_with_prev_result == "yes"