import json
import os

from users.user import User


class UserManager:

    USERS_FILE = "data/users.json"

    def __init__(self):

        self.users = {}
        self.load_users()

        # ---------------- DEFAULT ADMIN ----------------
        if "admin" not in self.users:
            self.users["admin"] = User("admin", "admin123", "admin")
            self.save_users()

    # ---------------- LOAD USERS ----------------

    def load_users(self):

        if not os.path.exists(self.USERS_FILE):
            return

        try:

            with open(self.USERS_FILE, "r", encoding="utf-8") as file:

                content = file.read().strip()

                if not content:
                    return

                data = json.loads(content)

                for username, details in data.items():

                    self.users[username] = User(
                        username,
                        details["password"],
                        details.get("role", "user")
                    )

        except Exception:
            self.users = {}

    # ---------------- SAVE USERS ----------------

    def save_users(self):

        data = {}

        for username, user in self.users.items():

            data[username] = {
                "password": user.password,
                "role": user.role
            }

        with open(self.USERS_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    # ---------------- ADD USER ----------------

    def add_user(self, username: str, password: str, role: str = "user"):

        if username in self.users:
            raise ValueError(f"User '{username}' already exists")

        self.users[username] = User(username, password, role)
        self.save_users()

    # ---------------- GET USER ----------------

    def get_user(self, username: str):

        return self.users.get(username)

    # ---------------- REMOVE USER (SAFE) ----------------

    def remove_user(self, username: str):

        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist")

        user = self.users[username]

        # 🔥 protect admin role (scalable approach)
        if user.role == "admin":
            raise PermissionError("Cannot delete admin user")

        del self.users[username]
        self.save_users()

    # ---------------- AUTH ----------------

    def authenticate(self, username: str, password: str):

        user = self.users.get(username)

        if not user:
            return None

        if user.password != password:
            return None

        return user