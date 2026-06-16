from commands.base_command import BaseCommand


class CdCommand(BaseCommand):

    def __init__(self, filesystem_service):
        self.filesystem_service = filesystem_service

    def execute(
        self,
        directory_name
    ):

        self.filesystem_service.cd(
            directory_name
        )