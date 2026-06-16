from commands.base_command import BaseCommand


class HelpCommand(BaseCommand):

    def execute(self):

        print("\n================= PYOS HELP =================\n")

        print("FILESYSTEM COMMANDS")
        print("-------------------")
        print("mkdir <dirname>               Create a directory")
        print("ls                            List files and folders")
        print("cd <dirname>                  Change directory")
        print("pwd                           Show current path")
        print("touch <filename>              Create a file")
        print("write <file> <content>        Write content to file")
        print("cat <file>                    Read file content")
        print("cp <source> <destination>     Copy file")
        print("mv <source> <destination>     Move/Rename file")
        print("rm <file/folder>              Delete file or folder")
        print("find <name>                   Search file/folder")
        print("tree                          Show directory tree")

        print("\nUSER COMMANDS")
        print("-------------")
        print("adduser <username> <password> Create new user")
        print("login <username> <password>   Login")
        print("logout                        Logout current user")
        print("whoami                        Show current user")
        print("deleteuser <username>         Delete user (Admin only)")

        print("\nSYSTEM COMMANDS")
        print("----------------")
        print("chmod <name> <perm>           Change permissions")
        print("history                       Show command history")
        print("clear                         Clear terminal screen")
        print("cls                           Clear terminal screen")
        print("help                          Show help menu")
        print("exit                          Exit PyOS")

        print("\n================================================\n")