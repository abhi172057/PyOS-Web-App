from filesystem_api.models import File, Directory
from recyclebin_api.models import RecycleBinItem
from filesystem_api.services.security_service import FileSystemSecurity
from history_api.services.history_service import HistoryService
from logs_api.services.log_service import LogService
from filesystem_api.models import Directory


class FileSystemService:

    @staticmethod
    def delete_file(file_id, owner):
        try:
            # ✅ FETCH WITH BASE SECURITY
            file = File.objects.get(id=file_id, owner=owner)

            # 🔐 EXTRA SECURITY LAYER
            if not FileSystemSecurity.can_write(owner, file):
                LogService.create_log(
                    "ERROR",
                    f"Delete denied: {file_id}",
                    owner
                )
                return False

            file_name = file.name
            file_content = file.content

            # 🗑 MOVE TO RECYCLE BIN
            RecycleBinItem.objects.create(
                owner=owner,
                item_name=file_name,
                item_type="file",
                content=file_content,
                parent_id=file.directory.id
            )

            # 🧨 DELETE FILE
            file.delete()

            # 📜 HISTORY LOG
            HistoryService.log_command(owner, f"rm {file_name}")

            # 📊 SYSTEM LOG
            LogService.create_log(
                "WARNING",
                f"File moved to recycle bin: {file_name}",
                owner
            )

            return True

        except File.DoesNotExist:
            LogService.create_log(
                "ERROR",
                f"Delete failed: file not found {file_id}",
                owner
            )
            return False
    

    @staticmethod
    def list_directory(directory_id, user):
        try:
            directory = Directory.objects.get(id=directory_id, owner=user)

            subdirs = Directory.objects.filter(parent=directory, owner=user)
            files = File.objects.filter(directory=directory, owner=user)

            return {
                "directory": directory,
                "directories": subdirs,
                "files": files
            }

        except Directory.DoesNotExist:
            return None
        
    @staticmethod
    def create_directory(name, owner, parent=None):

        directory = Directory.objects.create(
            name=name,
            owner=owner,
            parent=parent
        )

        HistoryService.log_command(
            owner,
            f"mkdir {name}"
        )

        LogService.create_log(
            "CREATE_DIRECTORY",
            f"Directory created: {name}",
            owner
        )

        return directory


    @staticmethod
    def create_file(name, content, owner, directory):

        file = File.objects.create(
            name=name,
            content=content,
            owner=owner,
            directory=directory
        )

        HistoryService.log_command(
            owner,
            f"touch {name}"
        )

        LogService.create_log(
            "CREATE_FILE",
            f"File created: {name}",
            owner
        )

    @staticmethod
    def move_file(file_id, destination_directory_id, owner):

        try:
            file = File.objects.get(
                id=file_id,
                owner=owner
            )

            destination = Directory.objects.get(
                id=destination_directory_id,
                owner=owner
            )

            old_directory = file.directory.name

            file.directory = destination
            file.save()

            HistoryService.log_command(
                owner,
                f"mv {file.name} {destination.name}"
            )

            LogService.create_log(
                "MOVE_FILE",
                f"File '{file.name}' moved from '{old_directory}' to '{destination.name}'",
                owner
            )

            return True

        except File.DoesNotExist:
            return False

        except Directory.DoesNotExist:
            return False    

        return file    
    
    @staticmethod
    def move_directory(
        directory_id,
        destination_directory_id,
        owner
    ):

        try:

            directory = Directory.objects.get(
                id=directory_id,
                owner=owner
            )

            destination = Directory.objects.get(
                id=destination_directory_id,
                owner=owner
            )

            directory.parent = destination
            directory.save()

            HistoryService.log_command(
                owner,
                f"mv-folder {directory.name} {destination.name}"
            )

            LogService.create_log(
                "MOVE_DIRECTORY",
                f"Directory '{directory.name}' moved to '{destination.name}'",
                owner
            )

            return True

        except Directory.DoesNotExist:
            return False
        
    @staticmethod
    def delete_directory(directory_id, owner):

        try:

            directory = Directory.objects.get(
                id=directory_id,
                owner=owner
            )

            RecycleBinItem.objects.create(
                owner=owner,
                item_name=directory.name,
                item_type="directory",
                parent_id=directory.parent.id if directory.parent else None
            )

            directory.delete()

            HistoryService.log_command(
                owner,
                f"rm-folder {directory.name}"
            )

            LogService.create_log(
                "DELETE_DIRECTORY",
                f"Directory moved to recycle bin: {directory.name}",
                owner
            )

            return True

        except Directory.DoesNotExist:
            return False    