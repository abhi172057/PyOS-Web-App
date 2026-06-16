from users.user import User


class Session:
    """
    Tracks current logged-in user.
    """

    def __init__(self):

        self.current_user = None

    def login(
        self,
        user: User
    ):

        self.current_user = user

    def logout(self):

        self.current_user = None

    def is_authenticated(
        self
    ) -> bool:

        return self.current_user is not None

    def get_current_user(
        self
    ):

        return self.current_user