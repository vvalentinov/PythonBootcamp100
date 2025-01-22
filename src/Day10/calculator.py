import art
import console_utils
import calculator_utils

print("Welcome to the Calculator Project!")
print(art.logo)

result = 0
continue_with_prev_result = False

while True:
    if continue_with_prev_result:
        first_number = result
    else:
        first_number = console_utils.get_number_input("What is your first number: ")

    operator = console_utils.get_operator_input()

    second_number = console_utils.get_number_input("What is your second number: ")

    result = calculator_utils.perform_calculation(operator, first_number, second_number)

    print(f"{first_number} {operator} {second_number} = {result}")

    if console_utils.get_exit_program_input():
        print("It was a pleasure! Till next time.")
        print(art.farewell)
        break

    continue_with_prev_result = console_utils.get_continue_with_prev_result_input(result)
