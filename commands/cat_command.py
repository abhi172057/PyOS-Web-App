from commands.base_command import BaseCommand


class CatCommand(BaseCommand):

    def __init__(self, filesystem_service):
        self.filesystem_service = filesystem_service

    def execute(self, filename):

        content = (
            self.filesystem_service
            .cat(filename)
        )

        print(content)