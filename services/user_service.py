import json
import os

from users.user import User
from core.session import Session


class UserService:

    USERS_FILE = "data/users.json"

    def __init__(self):

        self.users = {}
        self.session = Session()
        self.load_users()

        # ---------------- DEFAULT ADMIN FIX ----------------
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

    def add_user(self, username: str, password: str, role="user"):

        if username in self.users:
            raise ValueError(f"User '{username}' already exists")

        self.users[username] = User(username, password, role)
        self.save_users()

    # ---------------- LOGIN ----------------

    def login(self, username: str, password: str):

        if self.session.is_authenticated():
            self.session.logout()

        user = self.users.get(username)

        if not user or user.password != password:
            raise ValueError("Invalid credentials")

        self.session.login(user)

    # ---------------- LOGOUT ----------------

    def logout(self):
        self.session.logout()

    # ---------------- WHOAMI ----------------

    def whoami(self):

        user = self.session.get_current_user()

        if not user:
            return "Guest"

        return f"{user.username} ({user.role})"

    # ---------------- CHECK LOGIN ----------------

    def is_logged_in(self):
        return self.session.is_authenticated()

    # ---------------- ADMIN CHECK ----------------

    def is_admin(self):

        user = self.session.get_current_user()
        return user and user.role == "admin"

    # ---------------- REMOVE USER (SECURE) ----------------

    def remove_user(self, username: str):

        if not self.is_logged_in():
            raise PermissionError("Login required")

        current_user = self.session.get_current_user()

        if not current_user or current_user.role != "admin":
            raise PermissionError("Admin access required")

        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist")

        target_user = self.users[username]

        if target_user.role == "admin":
            raise PermissionError("Cannot delete admin user")

        del self.users[username]
        self.save_users()

    # ---------------- GET USER ----------------

    def get_user(self, username: str):
        return self.users.get(username)