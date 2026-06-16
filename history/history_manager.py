import json
import os


class HistoryManager:

    HISTORY_FILE = "data/history.json"

    def __init__(self):

        self.commands = []

        self.load_history()

    def add_command(
        self,
        command: str
    ):

        self.commands.append(command)

        self.save_history()

    def get_history(
        self
    ):

        return self.commands

    def save_history(
        self
    ):

        with open(
            self.HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.commands,
                file,
                indent=4
            )

    def load_history(
        self
    ):

        if not os.path.exists(
            self.HISTORY_FILE
        ):
            return

        try:

            with open(
                self.HISTORY_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read().strip()

                if not content:
                    self.commands = []
                    return

                self.commands = json.loads(
                    content
                )

        except Exception:

            self.commands = []