class LoggingMixin:  # Yeh ek mixin hai
    def log(self, message):  # Ek common function provide karta hai
        print(f"[LOG]: {message}")

class User:  # Normal ek user class
    def __init__(self, username):
        self.username = username

class Admin(User, LoggingMixin):  # User aur LoggingMixin dono se inherit kar raha hai
    def delete_user(self, user):
        # Mixin ka log method use ho raha hai
        self.log(f"Admin {self.username} deleted user {user.username}")

# Example Usage
admin = Admin("admin_user")  # Ek admin object banaya
user = User("regular_user")  # Ek user object banaya
admin.delete_user(user)  # Admin ka delete_user method call kiya
