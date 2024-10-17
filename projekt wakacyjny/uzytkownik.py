import json
from roles import Role

class MenagerUzytkownika:
    def __init__(self, data_file="data.json") -> None:
        self.data_file = data_file
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
            return data.get("users", [])
        except FileNotFoundError:
            return []

    def save_users(self):
        with open(self.data_file, "w") as file:
            json.dump({"users": self.users}, file, indent=4)

    def get_user(self, username):
        for user in self.users:
            if user["username"] == username:
                return user
        return None

    def add_user(self, username, role, password=None):
        if self.get_user(username) is None:
            if password is None:
                raise ValueError("Hasło musi być podane.")
            new_user = {"username": username, "role": role, "password": password}
            self.users.append(new_user)
            self.save_users()
            print(f"Użytkownik {username} dodany.")
        else:
            raise ValueError("Użytkownik o takiej nazwie już istnieje.")

    def update_user_role(self, username, new_role):
        user = self.get_user(username)
        if user:
            user["role"] = new_role
            self.save_users()
        else:
            raise ValueError("Nie znaleziono użytkownika.")
