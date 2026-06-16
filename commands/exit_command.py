from commands.base_command import BaseCommand
from storage.persistence import Persistence


class ExitCommand(BaseCommand):

    def __init__(self, filesystem_service):
        self.filesystem_service = filesystem_service

    def execute(self):

        Persistence.save_filesystem(
            self.filesystem_service.filesystem
        )

        print("Filesystem saved.")
        print("Shutting down PyOS...")

        raise SystemExit