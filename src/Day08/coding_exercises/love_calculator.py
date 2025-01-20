def calculate_love_score(first_name, second_name):
    total_true_letters = 0
    total_love_letters = 0
    first_name_lower = first_name.lower()
    second_name_lower = second_name.lower()
    for letter in first_name_lower:
        if letter in "true":
            total_true_letters += 1
        if letter in "love":
            total_love_letters += 1
    for letter in second_name_lower:
        if letter in "true":
            total_true_letters += 1
        if letter in "love":
            total_love_letters += 1

    print(f"{total_true_letters}{total_love_letters}")

calculate_love_score("Kanye West", "Kim Kardashian")