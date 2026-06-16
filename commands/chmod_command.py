from commands.base_command import BaseCommand


class ChmodCommand(BaseCommand):

    def __init__(self, fs_service):
        self.fs_service = fs_service

    def execute(self, mode, filename):

        # validate mode first (important safety check)
        if not mode.isdigit() or len(mode) != 3:
            raise ValueError("Invalid permission format. Use 755, 644 etc.")

        file = self.fs_service.get_file(filename)

        file.permissions.set_from_octal(mode)

        print(f"Permissions updated: {filename} -> {mode}")