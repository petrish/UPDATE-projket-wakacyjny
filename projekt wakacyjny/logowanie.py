class Auth:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def login(self, username, password):
        user = self.user_manager.get_user(username)
        if user:
            if user.get('password') == password:
                print(f"Zalogowano jako {username} ({user['role']})")
                return user
            else:
                raise ValueError("Nieprawidłowe hasło.")
        else:
            raise ValueError("Nieprawidłowa nazwa użytkownika.")
