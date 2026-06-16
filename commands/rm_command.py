from commands.base_command import BaseCommand


class RmCommand(BaseCommand):

    def __init__(self, filesystem_service):
        self.filesystem_service = filesystem_service

    def execute(self, name=None):

        if not name:
            raise ValueError("rm requires a filename or directory name")

        # Let filesystem handle validation + deletion
        self.filesystem_service.rm(name)

        print(f"'{name}' removed.")