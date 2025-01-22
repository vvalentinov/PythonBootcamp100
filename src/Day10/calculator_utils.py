def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1 ,n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def perform_calculation(operator, first_number, second_number):
    if operator == "+":
        result = add(first_number, second_number)
    elif operator == "-":
        result = subtract(first_number, second_number)
    elif operator == "*":
        result = multiply(first_number, second_number)
    else:
        result = division(first_number, second_number)

    return  result
