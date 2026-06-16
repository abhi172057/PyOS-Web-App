class Parser:
    """
    Converts user input into
    command name + arguments.
    """

    def parse(self, user_input: str):

        user_input = user_input.strip()

        if not user_input:
            return None, []

        tokens = user_input.split()

        command_name = tokens[0]

        args = tokens[1:]

        return command_name, args