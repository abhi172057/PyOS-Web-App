from filesystem.directory import Directory
from filesystem.file import File
from storage.persistence import Persistence


class FileSystem:

    def __init__(self):

        loaded_root = Persistence.load_filesystem()

        if loaded_root:
            self.root = loaded_root
        else:
            self.root = Directory("root")

        self.current_directory = self.root

    # ---------------- DIRECTORY OPS ----------------

    def mkdir(self, name: str):
        if "/" in name:
            raise ValueError("Use cd first, nested mkdir not supported")

        if self.current_directory.has_child(name):
            raise ValueError(f"{name} already exists")

        directory = Directory(name)
        self.current_directory.add_child(directory)

    def touch(self, filename: str):

        file = File(filename)
        self.current_directory.add_child(file)

    def ls(self):
        return self.current_directory.list_children()

    def pwd(self) -> str:
        return self.current_directory.get_path()

    def cd(self, path: str):

        if path == "..":
            if self.current_directory.parent:
                self.current_directory = self.current_directory.parent
            return

        parts = path.split("/")
        current = self.current_directory

        for part in parts:

            if part in ["", "."]:
                continue

            next_node = current.get_child(part)

            if next_node is None:
                raise FileNotFoundError(part)

            if not isinstance(next_node, Directory):
                raise NotADirectoryError(part)

            current = next_node

        self.current_directory = current

    # ---------------- FILE OPS ----------------

    def write(self, filename: str, content: str):

        parent, name = self.resolve_parent_and_name(filename)

        if parent is None:
            raise FileNotFoundError(filename)

        file = parent.get_child(name)

        if file is None:
            raise FileNotFoundError(filename)

        file.write(content)

    def cat(self, filename: str):

        parent, name = self.resolve_parent_and_name(filename)

        if parent is None:
            raise FileNotFoundError(filename)

        file = parent.get_child(name)

        if file is None:
            raise FileNotFoundError(filename)

        return file.read()

    # ---------------- PATH RESOLVER (IMPORTANT FIX) ----------------

    def resolve_parent_and_name(self, path: str):

        parts = path.split("/")
        current = self.root

        for part in parts[:-1]:

            if part == "":
                continue

            next_node = current.get_child(part)

            if next_node is None:
                return None, None

            current = next_node

        return current, parts[-1]

    # ---------------- COPY FILE ----------------

    def copy_file(self, source: str, destination: str, force: bool = False):

        file = self.current_directory.get_child(source)

        if file is None:
            raise FileNotFoundError(source)

        if not isinstance(file, File):
            raise ValueError("Can only copy files")

        existing = self.current_directory.get_child(destination)

        if existing and not force:
            raise FileExistsError(f"{destination} already exists")

        copied_file = File(destination)
        copied_file.content = file.content

        self.current_directory.add_child(copied_file)

    # ---------------- FIXED RM (IMPORTANT FIX) ----------------

    def rm(self, name: str):

        # CASE 1: simple name in current directory
        node = self.current_directory.get_child(name)

        if node:
            self.current_directory.remove_child(name)
            return

        # CASE 2: PATH like test/a.txt
        parent, filename = self.resolve_parent_and_name(name)

        if parent is None:
            raise FileNotFoundError(f"{name} not found")

        node = parent.get_child(filename)

        if node is None:
            raise FileNotFoundError(f"{name} not found")

        parent.remove_child(filename)

    # ---------------- FIXED MV ----------------

    def mv(self, source: str, destination: str):

        file = self.current_directory.get_child(source)

        if file is None:
            raise FileNotFoundError(source)

        if not isinstance(file, File):
            raise ValueError("Can only move files")

        # remove from current location
        self.current_directory.remove_child(source)

        # resolve destination path
        parts = destination.split("/")
        new_name = parts[-1]

        target_dir = self.current_directory

        for folder in parts[:-1]:

            if folder == "":
                continue

            next_dir = target_dir.get_child(folder)

            if next_dir is None:
                raise FileNotFoundError(folder)

            target_dir = next_dir

        if target_dir.has_child(new_name):
            raise FileExistsError(f"{new_name} already exists")

        file.name = new_name
        target_dir.add_child(file)

    # ---------------- FIND ----------------

    def find(self, name: str):

        results = []

        def dfs(node, path):

            current_path = "/" + node.name if node.name != "root" else ""

            if node.name == name:
                results.append(current_path if current_path else "/")

            if hasattr(node, "children"):
                for child in node.children.values():
                    dfs(child, current_path)

        dfs(self.root, "")

        return results

    # ---------------- TREE ----------------

    def tree(self, node=None):

        if node is None:
            node = self.root

        print(node.name)

        def dfs(current, prefix=""):

            children = list(current.children.values()) if hasattr(current, "children") else []

            for i, child in enumerate(children):

                last = i == len(children) - 1
                branch = "└── " if last else "├── "

                print(prefix + branch + child.name)

                if hasattr(child, "children"):
                    new_prefix = prefix + ("    " if last else "│   ")
                    dfs(child, new_prefix)

        dfs(node)