from commands.base_command import BaseCommand


class AddUserCommand(BaseCommand):

    def __init__(self, user_service):
        self.user_service = user_service

    def execute(self, username=None, password=None):

        if not username or not password:
            print(
                "Usage: adduser <username> <password>"
            )
            return

        self.user_service.add_user(
            username,
            password
        )

        print(
            f"User '{username}' created."
        )