# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# with open("new_file.txt", mode="w") as file:
#     file.write("A new .txt file has been created.")

# Read file from desktop
# with open("/Users/user/Desktop/file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("C:\\Users\\user\\Desktop\\file.txt") as file:
    contents = file.read()
    print(contents)