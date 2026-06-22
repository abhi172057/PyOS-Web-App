from logs_api.models import LogEntry


class LogService:

    # =========================
    # CREATE LOG
    # =========================
    @staticmethod
    def create_log(action, description, user=None):

        if not user:
            return None

        return LogEntry.objects.create(
            user=user,
            action=action,
            description=description
        )

    # =========================
    # GET ALL LOGS
    # =========================
    @staticmethod
    def get_logs():

        return LogEntry.objects.all().order_by('-id')

    # =========================
    # GET USER LOGS
    # =========================
    @staticmethod
    def get_user_logs(user):

        return LogEntry.objects.filter(
            user=user
        ).order_by('-id')