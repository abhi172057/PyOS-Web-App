from commands.base_command import BaseCommand


class TreeCommand(BaseCommand):

    def __init__(self, fs_service):
        self.fs_service = fs_service

    def execute(self):

        output = self.fs_service.tree()
        