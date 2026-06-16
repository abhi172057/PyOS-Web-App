from filesystem.node import Node


class Directory(Node):

    def __init__(self, name: str):
        super().__init__(name)
        self.children: dict = {}

    # -------------------------
    # ADD CHILD (SAFE)
    # -------------------------
    def add_child(self, node):

        if node.name in self.children:
            raise ValueError(f"{node.name} already exists")

        # 🔥 safety check: prevent multiple parents
        if node.parent is not None:
            raise ValueError(f"{node.name} already belongs to another directory")

        node.parent = self
        self.children[node.name] = node

    # -------------------------
    # REMOVE CHILD (FIXED)
    # -------------------------
    def remove_child(self, name: str):

        if name not in self.children:
            raise FileNotFoundError(f"{name} not found")

        node = self.children[name]

        # 🔥 IMPORTANT FIX: break parent link
        node.parent = None

        del self.children[name]

    # -------------------------
    # GET CHILD
    # -------------------------
    def get_child(self, name: str):
        return self.children.get(name)

    # -------------------------
    # CHECK CHILD
    # -------------------------
    def has_child(self, name: str) -> bool:
        return name in self.children

    # -------------------------
    # LIST CHILDREN
    # -------------------------
    def list_children(self):
        return list(self.children.values())

    # -------------------------
    # STRING REPRESENTATION
    # -------------------------
    def __str__(self):
        return f"DIR: {self.name}"

    # -------------------------
    # PATH (FIXED & SAFE)
    # -------------------------
    def get_path(self):
        if self.parent is None:
            return "/" if self.name == "root" else f"/{self.name}"

        return self.parent.get_path().rstrip("/") + "/" + self.name