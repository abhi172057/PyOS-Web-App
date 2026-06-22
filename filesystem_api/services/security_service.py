class FileSystemSecurity:

    # =========================
    # ADMIN CHECK
    # =========================
    @staticmethod
    def is_admin(user):
        return (
            user is not None and
            user.is_authenticated and
            hasattr(user, "profile") and
            user.profile.role == "ADMIN"
        )

    # =========================
    # OWNER CHECK
    # =========================
    @staticmethod
    def is_owner(user, obj):
        return (
            user is not None and
            hasattr(obj, "owner") and
            obj.owner == user
        )

    # =========================
    # READ ACCESS
    # =========================
    @staticmethod
    def can_read(user, obj):

        if FileSystemSecurity.is_admin(user):
            return True

        return FileSystemSecurity.is_owner(user, obj)

    # =========================
    # WRITE ACCESS
    # =========================
    @staticmethod
    def can_write(user, obj):

        if FileSystemSecurity.is_admin(user):
            return True

        return FileSystemSecurity.is_owner(user, obj)

    # =========================
    # DELETE ACCESS
    # =========================
    @staticmethod
    def can_delete(user, obj):

        if FileSystemSecurity.is_admin(user):
            return True

        return FileSystemSecurity.is_owner(user, obj)

    # =========================
    # DIRECTORY ACCESS (EXPLICIT)
    # =========================
    @staticmethod
    def can_access_directory(user, directory):

        return FileSystemSecurity.can_read(user, directory)