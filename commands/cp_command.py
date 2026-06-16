from commands.base_command import BaseCommand


class CpCommand(BaseCommand):

    def __init__(
        self,
        fs_service
    ):
        self.fs_service = fs_service

    def execute(
        self,
        source,
        destination
    ):

        self.fs_service.copy_file(
            source,
            destination
        )

        print(
            f"Copied '{source}' -> '{destination}'"
        )