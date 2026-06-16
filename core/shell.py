from commands.chmod_command import ChmodCommand
from core.parser import Parser

from services.logger_service import LoggerService
from services.filesystem_service import FileSystemService
from services.user_service import UserService

from history.history_manager import HistoryManager

from commands.mkdir_command import MkdirCommand
from commands.ls_command import LsCommand
from commands.cp_command import CpCommand
from commands.cd_command import CdCommand
from commands.pwd_command import PwdCommand
from commands.touch_command import TouchCommand
from commands.write_command import WriteCommand
from commands.cat_command import CatCommand
from commands.rm_command import RmCommand
from commands.mv_command import MvCommand
from commands.find_command import FindCommand
from commands.tree_command import TreeCommand

from commands.help_command import HelpCommand
from commands.history_command import HistoryCommand

from commands.adduser_command import AddUserCommand
from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand
from commands.whoami_command import WhoAmICommand
from commands.deleteuser_command import DeleteUserCommand

from commands.clear_command import ClearCommand   # ✅ FIXED (correct file)

from commands.exit_command import ExitCommand


class Shell:

    def __init__(self):

        self.parser = Parser()
        self.logger = LoggerService()
        self.fs_service = FileSystemService()
        self.user_service = UserService()
        self.history_manager = HistoryManager()

        self.commands = {

            # ---------------- FILESYSTEM ----------------
            "mkdir": MkdirCommand(self.fs_service),
            "ls": LsCommand(self.fs_service),
            "cp": CpCommand(self.fs_service),
            "cd": CdCommand(self.fs_service),
            "pwd": PwdCommand(self.fs_service),
            "touch": TouchCommand(self.fs_service),
            "write": WriteCommand(self.fs_service),
            "cat": CatCommand(self.fs_service),
            "rm": RmCommand(self.fs_service),
            "mv": MvCommand(self.fs_service),
            "find": FindCommand(self.fs_service),
            "tree": TreeCommand(self.fs_service),

            # ---------------- SYSTEM ----------------
            "clear": ClearCommand(self.fs_service),   # ✅ FIXED
            "cls": ClearCommand(self.fs_service),     # ✅ FIXED
            "chmod": ChmodCommand(self.fs_service),
            "exit": ExitCommand(self.fs_service),

            # ---------------- HISTORY ----------------
            "history": HistoryCommand(self.history_manager),

            # ---------------- USER SYSTEM ----------------
            "adduser": AddUserCommand(self.user_service),
            "login": LoginCommand(self.user_service),
            "logout": LogoutCommand(self.user_service),
            "whoami": WhoAmICommand(self.user_service),
            "deleteuser": DeleteUserCommand(self.user_service),

            # ---------------- MISC ----------------
            "help": HelpCommand()
        }

    def run(self):

        print("\nPyOS Started")
        print("Type 'help'")

        while True:

            try:
                current_path = self.fs_service.pwd()
                user_input = input(f"\nPyOS:{current_path}> ")

                command_name, args = self.parser.parse(user_input)

                if not command_name:
                    continue

                command = self.commands.get(command_name)

                if command is None:
                    print("Unknown command")
                    continue

                # ---------------- AUTH CHECK ----------------
                if not self.require_auth(command_name):
                    continue

                # ---------------- USER ----------------
                user = self.safe_user()

                # ---------------- LOGGING ----------------
                try:
                    self.logger.log(user, user_input)
                    self.history_manager.add_command(f"{user} > {user_input}")
                except Exception:
                    pass

                # ---------------- EXECUTION ----------------
                try:
                    if args is None:
                        command.execute()

                    elif isinstance(args, (list, tuple)):
                        command.execute(*args)

                    else:
                        command.execute(args)

                except TypeError as te:
                    print(f"Error: Invalid arguments - {te}")

            except Exception as e:
                print(f"[Runtime Error] {e}")

    # ---------------- AUTH RULES ----------------
    def require_auth(self, command_name):

        allowed_without_login = {
            "login",
            "adduser",
            "help",
            "exit",
            "whoami",
            "clear",
            "cls"
        }

        if command_name in allowed_without_login:
            return True

        if not self.user_service.is_logged_in():
            print("Error: Please login first.")
            return False

        return True

    # ---------------- SAFE USER ----------------
    def safe_user(self):

        try:
            return self.user_service.whoami()
        except Exception:
            return "Guest"