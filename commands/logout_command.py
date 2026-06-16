from commands.base_command import BaseCommand


class LogoutCommand(BaseCommand):

    def __init__(self, user_service):
        self.user_service = user_service

    def execute(self):

        self.user_service.logout()

        print("Logged out")