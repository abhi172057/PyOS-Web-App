from filesystem.filesystem import FileSystem
from filesystem.file import File
from filesystem.directory import Directory


class FileSystemService:

    def __init__(self):
        self.filesystem = FileSystem()

    # ---------------- BASIC OPS ----------------

    def mkdir(self, name: str):
        self.filesystem.mkdir(name)

    def touch(self, filename: str):
        self.filesystem.touch(filename)

    def ls(self):
        return self.filesystem.ls()

    def cd(self, path: str):
        self.filesystem.cd(path)

    def pwd(self):
        return self.filesystem.pwd()

    def write(self, filename: str, content: str):
        self.filesystem.write(filename, content)

    def cat(self, filename: str):
        return self.filesystem.cat(filename)

    def copy_file(self, source, destination, force=False):
        self.filesystem.copy_file(source, destination, force)

    def rm(self, name: str):
        if not name:
            raise ValueError("rm requires a file or directory name")
        self.filesystem.rm(name)

    def mv(self, source, destination):
        if not source or not destination:
            raise ValueError("mv requires source and destination")
        self.filesystem.mv(source, destination)

    def find(self, name: str):
        return self.filesystem.find(name)

    def tree(self):
        return self.filesystem.tree()

    # ---------------- SAFE NODE ACCESS ----------------

    def get_node(self, name: str):

        if not name:
            raise ValueError("Name cannot be empty")

        node = self.filesystem.current_directory.get_child(name)

        if node is None:
            raise FileNotFoundError(f"{name} not found")

        return node

    def get_file(self, filename: str):

        node = self.get_node(filename)

        if not isinstance(node, File):
            raise TypeError(f"{filename} is not a file")

        return node

    def get_directory(self, dirname: str):

        node = self.get_node(dirname)

        if not isinstance(node, Directory):
            raise TypeError(f"{dirname} is not a directory")

        return node

    # ---------------- FUTURE READY ----------------

    def resolve_path(self, path: str):
        """
        (NOT YET USED BUT IMPORTANT)
        Will support:
        /docs/a.txt
        ../file.txt
        """
        return path