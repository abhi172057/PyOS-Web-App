from storage.json_store import (
    JsonStore
)

from storage.serializer import (
    Serializer
)


class Persistence:

    FILESYSTEM_PATH = (
        "data/filesystem.json"
    )

    @classmethod
    def save_filesystem(
        cls,
        filesystem
    ):

        data = (
            Serializer.serialize_node(
                filesystem.root
            )
        )

        JsonStore.save(
            cls.FILESYSTEM_PATH,
            data
        )

    @classmethod
    def load_filesystem(
        cls
    ):

        data = JsonStore.load(
            cls.FILESYSTEM_PATH
        )

        if not data:
            return None

        return (
            Serializer.deserialize_node(
                data
            )
        )