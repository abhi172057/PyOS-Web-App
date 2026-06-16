from commands.base_command import BaseCommand


class WhoAmICommand(BaseCommand):

    def __init__(self, user_service):
        self.user_service = user_service

    def execute(self):

        print(self.user_service.whoami())