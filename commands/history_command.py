from commands.base_command import (
    BaseCommand
)


class HistoryCommand(
    BaseCommand
):

    def __init__(
        self,
        history_manager
    ):
        self.history_manager = (
            history_manager
        )

    def execute(self):

        history = (
            self.history_manager
            .get_history()
        )

        if not history:

            print(
                "No commands found."
            )

            return

        for index, command in enumerate(
            history,
            start=1
        ):

            print(
                f"{index}. {command}"
            )