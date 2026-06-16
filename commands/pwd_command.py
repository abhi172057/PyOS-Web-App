from commands.base_command import BaseCommand


class PwdCommand(BaseCommand):

    def __init__(self, filesystem_service):
        self.filesystem_service = filesystem_service

    def execute(self):

        print(
            self.filesystem_service.pwd()
        )