import json
import os

from datetime import datetime


class LoggerService:

    LOG_FILE = "data/logs.json"

    def __init__(self):

        if not os.path.exists(
            self.LOG_FILE
        ):

            with open(
                self.LOG_FILE,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )

    def log(
        self,
        username,
        action
    ):

      
        try:

            with open(
                self.LOG_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                content = (
                    file.read().strip()
                )

                logs = (
                    json.loads(content)
                    if content
                    else []
                )

        except Exception as e:

            logs = []

        logs.append({

            "time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "user":
                username,

            "action":
                action
        })

        with open(
            self.LOG_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                logs,
                file,
                indent=4
            )
