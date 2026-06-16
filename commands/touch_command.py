from commands.base_command import BaseCommand


class TouchCommand(BaseCommand):

    def __init__(self, filesystem_service):
        self.filesystem_service = filesystem_service

    def execute(self, filename):

        self.filesystem_service.touch(
            filename
        )

        print(
            f"File '{filename}' created."
        )