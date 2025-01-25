def odd_or_even(number):
    # We need to use the "==" (not "=") sign to check if the remainder is zero
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."