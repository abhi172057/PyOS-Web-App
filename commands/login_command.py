from commands.base_command import BaseCommand


class LoginCommand(BaseCommand):

    def __init__(self, user_service):
        self.user_service = user_service

    def execute(self, username, password):

        self.user_service.login(username, password)

        print(f"Logged in as {username}")