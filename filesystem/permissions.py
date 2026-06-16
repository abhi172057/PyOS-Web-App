class Permissions:

    def __init__(self):

        # rwx for owner, group, others
        self.owner = {
            "r": True,
            "w": True,
            "x": False
        }

        self.group = {
            "r": True,
            "w": False,
            "x": False
        }

        self.others = {
            "r": True,
            "w": False,
            "x": False
        }

    # ----------------------------
    # COMPATIBILITY PROPERTIES
    # ----------------------------

    @property
    def read(self):
        return self.owner["r"]

    @property
    def write(self):
        return self.owner["w"]

    @property
    def execute(self):
        return self.owner["x"]

    # ----------------------------
    # SET PERMISSIONS (chmod 755)
    # ----------------------------

    def set_from_octal(
        self,
        value: str
    ):

        mapping = {
            "0": (False, False, False),
            "1": (False, False, True),
            "2": (False, True, False),
            "3": (False, True, True),
            "4": (True, False, False),
            "5": (True, False, True),
            "6": (True, True, False),
            "7": (True, True, True),
        }

        if len(value) != 3:
            raise ValueError(
                "Permission must be 3 digits like 755"
            )

        if not value.isdigit():
            raise ValueError(
                "Permission must be numeric like 755"
            )

        o, g, p = value

        self.owner = dict(
            zip(
                ["r", "w", "x"],
                mapping[o]
            )
        )

        self.group = dict(
            zip(
                ["r", "w", "x"],
                mapping[g]
            )
        )

        self.others = dict(
            zip(
                ["r", "w", "x"],
                mapping[p]
            )
        )

    # ----------------------------
    # PERMISSION CHECK HELPERS
    # ----------------------------

    def can_read(
        self,
        role="owner"
    ):
        return self._get_role(role)["r"]

    def can_write(
        self,
        role="owner"
    ):
        return self._get_role(role)["w"]

    def can_execute(
        self,
        role="owner"
    ):
        return self._get_role(role)["x"]

    # ----------------------------
    # INTERNAL HELPER
    # ----------------------------

    def _get_role(
        self,
        role
    ):

        if role == "owner":
            return self.owner

        elif role == "group":
            return self.group

        else:
            return self.others

    # ----------------------------
    # STRING FORMAT
    # ----------------------------

    def __str__(self):

        def rwx(block):

            return (
                ("r" if block["r"] else "-")
                + ("w" if block["w"] else "-")
                + ("x" if block["x"] else "-")
            )

        return (
            rwx(self.owner)
            + rwx(self.group)
            + rwx(self.others)
        )