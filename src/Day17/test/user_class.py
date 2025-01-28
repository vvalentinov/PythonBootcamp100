class User:

    def __init__(self, user_id, username):
        print(f"User {username} being created...")
        self.id = user_id
        self.username = username
        self.followers_count = 0
        self.following_count = 0

    def follow(self, user):
        self.following_count += 1
        user.followers_count += 1