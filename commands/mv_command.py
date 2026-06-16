from commands.base_command import BaseCommand


class MvCommand(BaseCommand):

    def __init__(self, fs_service):
        self.fs_service = fs_service

    def execute(self, source=None, destination=None):

        # ---------------- VALIDATION ----------------
        if not source or not destination:
            raise ValueError("mv requires source and destination")

        # ---------------- MOVE OPERATION ----------------
        self.fs_service.mv(source, destination)

        print(f"Moved/Renamed '{source}' -> '{destination}'")