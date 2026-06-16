from commands.base_command import BaseCommand


class LsCommand(BaseCommand):

    def __init__(self, filesystem_service):
        self.filesystem_service = filesystem_service

    def execute(self):

        items = (
            self.filesystem_service.ls()
        )

        if not items:
            print("Empty")

        for item in items:
            print(item)