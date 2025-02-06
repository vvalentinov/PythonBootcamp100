with open("file1.txt") as file_one:
    file_one_lines = [number_string.strip() for number_string in file_one.readlines()]
    file_one_numbers = [int(number) for number in file_one_lines]

with open("file2.txt") as file_two:
    file_two_lines = [number_string.strip() for number_string in file_two.readlines()]
    file_two_numbers = [int(number) for number in file_two_lines]

result = [x for x in file_one_numbers if x in file_two_numbers]
print(result)