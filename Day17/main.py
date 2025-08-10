class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        
    def follow(self, user):
        


user_1 = User("001","neil")

print(user_1.user_id)