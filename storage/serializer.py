from filesystem.directory import Directory
from filesystem.file import File


class Serializer:

    @staticmethod
    def serialize_node(node):

        if isinstance(node, File):

            return {
                "type": "file",
                "name": node.name,
                "content": node.content
            }

        return {
            "type": "directory",
            "name": node.name,
            "children": [
                Serializer.serialize_node(
                    child
                )
                for child in node.children.values()
            ]
        }

    @staticmethod
    def deserialize_node(data):

        if data["type"] == "file":

            file = File(
                data["name"]
            )

            file.content = data.get(
                "content",
                ""
            )

            return file

        directory = Directory(
            data["name"]
        )

        for child_data in data.get(
            "children",
            []
        ):

            child = (
                Serializer
                .deserialize_node(
                    child_data
                )
            )

            directory.add_child(
                child
            )

        return directory