from user_class import User

user_1 = User("001", "Valentin")
user_2 = User("002", "James")
print(f"User 1 with {user_1.id} id and {user_1.username} username.")
print(f"User 2 with {user_2.id} id and {user_2.username} username.")

user_2.follow(user_1)

print(f"{user_1.username} has {user_1.followers_count} followers and {user_2.username} is following {user_2.following_count} people.")