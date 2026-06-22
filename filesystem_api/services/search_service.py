from filesystem_api.models import File, Directory
from history_api.services.history_service import HistoryService
from logs_api.services.log_service import LogService


class SearchService:

    # =========================
    # SEARCH FILES ONLY
    # =========================
    @staticmethod
    def search_files(query, user):

        HistoryService.log_command(user, f"search file {query}")
        LogService.create_log("INFO", f"File search: {query}", user)

        return File.objects.filter(
            name__icontains=query,
            owner=user
        )

    # =========================
    # SEARCH DIRECTORIES ONLY
    # =========================
    @staticmethod
    def search_directories(query, user):

        HistoryService.log_command(user, f"search dir {query}")
        LogService.create_log("INFO", f"Directory search: {query}", user)

        return Directory.objects.filter(
            name__icontains=query,
            owner=user
        )

    # =========================
    # GLOBAL SEARCH (FILES + DIRS)
    # =========================
    @staticmethod
    def global_search(query, user):

        HistoryService.log_command(user, f"search global {query}")
        LogService.create_log("INFO", f"Global search executed: {query}", user)

        files = File.objects.filter(
            name__icontains=query,
            owner=user
        )

        directories = Directory.objects.filter(
            name__icontains=query,
            owner=user
        )

        return {
            "files": files,
            "directories": directories
        }