list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(string_number) for string_number in list_of_strings]
result = [number for number in numbers if number % 2 == 0]
print(result)