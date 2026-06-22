from history_api.models import CommandHistory


class HistoryService:

    # =========================
    # LOG COMMAND
    # =========================
    @staticmethod
    def log_command(user, command):

        if not user:
            return None

        return CommandHistory.objects.create(
            user=user,
            command=command
        )

    # =========================
    # GET USER HISTORY
    # =========================
    @staticmethod
    def get_user_history(user):

        if not user:
            return CommandHistory.objects.none()

        return CommandHistory.objects.filter(
            user=user
        ).order_by('-id')

    # =========================
    # FILTER HISTORY
    # =========================
    @staticmethod
    def filter_history(user, keyword):

        if not user:
            return CommandHistory.objects.none()

        return CommandHistory.objects.filter(
            user=user,
            command__icontains=keyword
        ).order_by('-id')

    # =========================
    # CLEAR HISTORY
    # =========================
    @staticmethod
    def clear_history(user):

        if not user:
            return False

        CommandHistory.objects.filter(
            user=user
        ).delete()

        return True