from commands.base_command import BaseCommand


class WriteCommand(BaseCommand):

    def __init__(self, filesystem_service):
        self.filesystem_service = filesystem_service

    def execute(self, filename, *content_parts):

        content = " ".join(content_parts)

        self.filesystem_service.write(
            filename,
            content
        )

        print(f"Written to '{filename}'.")