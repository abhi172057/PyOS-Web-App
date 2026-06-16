from __future__ import annotations

from datetime import datetime
from typing import Optional


class Node:
    """
    Base class for all filesystem entities (File, Directory).
    """

    def __init__(self, name: str):
        self.name: str = name
        self.parent: Optional["Node"] = None
        self.created_at: datetime = datetime.now()

    def get_path(self) -> str:
        """
        Returns absolute path of current node in filesystem tree.
        Example: /abhi/demo/file.txt
        """

        path_parts = []
        current = self

        # Traverse upward to root
        while current is not None:
            # skip root name to avoid /root/abhi style duplication
            if current.parent is not None:
                path_parts.append(current.name)
            current = current.parent

        # reverse to build correct order
        path_parts.reverse()

        return "/" + "/".join(path_parts)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name