from commands.base_command import BaseCommand


class DeleteUserCommand(BaseCommand):

    def __init__(self, user_service):
        self.user_service = user_service

    def execute(self, username):

        self.user_service.remove_user(username)
        print(f"User '{username}' deleted.")