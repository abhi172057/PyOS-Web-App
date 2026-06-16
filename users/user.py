from datetime import datetime


class User:
    """
    Represents a system user in PyOS.
    """

    def __init__(
        self,
        username: str,
        password: str,
        role: str = "user"
    ):

        self.username = username
        self.password = password

        # 🔥 role system (user / admin)
        self.role = role if role else "user"

        # metadata
        self.created_at = datetime.now()

        # user home directory (future feature ready)
        self.home_directory = f"/home/{username}"

    # ---------------- HELPERS ----------------

    def is_admin(self):
        return self.role == "admin"

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"User(username={self.username}, role={self.role})"