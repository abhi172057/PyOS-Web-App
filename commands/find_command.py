from commands.base_command import BaseCommand


class FindCommand(BaseCommand):

    def __init__(self, filesystem_service):
        self.fs = filesystem_service

    def execute(self, name):

        results = self.fs.find(name)

        if not results:
            print(f"No file or directory found: {name}")
            return

        for r in results:
            print(r)