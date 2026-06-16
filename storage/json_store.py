import json
import os


class JsonStore:

    @staticmethod
    def save(filepath, data):

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    @staticmethod
    def load(filepath):

        if not os.path.exists(filepath):
            return None

        try:

            with open(
                filepath,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read().strip()

                if not content:
                    return None

                return json.loads(content)

        except json.JSONDecodeError:
            return None