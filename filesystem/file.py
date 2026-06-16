from filesystem.node import Node
from filesystem.permissions import Permissions


class File(Node):

    def __init__(self, name: str, owner: str = "system"):
        super().__init__(name)

        self.owner = owner
        self.content = ""

        # 🔐 proper permission system (OOP)
        self.permissions = Permissions()

    def read(self) -> str:

        if not self.permissions.read:
            raise PermissionError("Read permission denied")

        return self.content

    def write(self, content: str) -> None:

        if not self.permissions.write:
            raise PermissionError("Write permission denied")

        self.content = content

    def append(self, content: str) -> None:

        if not self.permissions.write:
            raise PermissionError("Write permission denied")

        self.content += content

    def clear(self) -> None:
        self.content = ""

    def __str__(self):
        return f"FILE: {self.name}"