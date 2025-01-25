# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
    # The for loop is iterating through the numbers between 1 and 19.
    # On each iteration it checks if the current one is the last one (20th) and if so it prints "You got it"
# 2. When is the function meant to print "You got it"?
    # The function prints "You got it" when the value of "i" is equal to 20
# 3. What are your assumptions about the value of i?
    # The value of "i" changes on each iteration - it starts as 1 but ends as 19.
    # The problem is that the "if check" will always be False, since the value of "i" will never reach 20.

# Solution
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()
