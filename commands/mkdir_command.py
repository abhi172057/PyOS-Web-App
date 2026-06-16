from commands.base_command import BaseCommand


class MkdirCommand(BaseCommand):

    def __init__(self, filesystem_service):
        self.filesystem_service = filesystem_service

    def execute(self, directory_name):

        self.filesystem_service.mkdir(
            directory_name
        )

        print(
            f"Directory '{directory_name}' created."
        )