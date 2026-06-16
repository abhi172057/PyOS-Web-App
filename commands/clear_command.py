from commands.base_command import BaseCommand


class ClearCommand(BaseCommand):

    def __init__(self, filesystem_service=None):
        self.filesystem_service = filesystem_service

    def execute(self, *args):
        # clear terminal screen
        print("\033c", end="")