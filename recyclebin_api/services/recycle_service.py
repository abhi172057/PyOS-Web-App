from filesystem_api.models import File, Directory
from recyclebin_api.models import RecycleBinItem
from history_api.services.history_service import HistoryService
from logs_api.services.log_service import LogService


class RecycleService:

    # =========================
    # LIST RECYCLE BIN
    # =========================
    @staticmethod
    def get_bin(owner):
        return RecycleBinItem.objects.filter(
            owner=owner
        ).order_by('-id')

    # =========================
    # RESTORE ITEM
    # =========================
    @staticmethod
    def restore_item(item_id, owner):

        try:
            item = RecycleBinItem.objects.get(
                id=item_id,
                owner=owner
            )

            # FILE RESTORE
            if item.item_type == "file":

                existing_file = File.objects.filter(
                    name=item.item_name,
                    owner=owner,
                    directory_id=item.parent_id
                ).first()

                if existing_file:

                    LogService.create_log(
                        "WARNING",
                        f"Restore failed, file already exists: {item.item_name}",
                        owner
                    )

                    return False

                File.objects.create(
                    name=item.item_name,
                    content=item.content,
                    owner=owner,
                    directory_id=item.parent_id
                )

                HistoryService.log_command(
                    owner,
                    f"restore file {item.item_name}"
                )

                LogService.create_log(
                    "CREATE_FILE",
                    f"File restored: {item.item_name}",
                    owner
                )

            # DIRECTORY RESTORE
            elif item.item_type == "directory":

                Directory.objects.create(
                    name=item.item_name,
                    owner=owner,
                    parent_id=item.parent_id
                )

                HistoryService.log_command(
                    owner,
                    f"restore dir {item.item_name}"
                )

                LogService.create_log(
                    "CREATE_DIRECTORY",
                    f"Directory restored: {item.item_name}",
                    owner
                )

            item.delete()

            return True

        except RecycleBinItem.DoesNotExist:
            return False

    # =========================
    # PERMANENT DELETE
    # =========================
    @staticmethod
    def permanent_delete(item_id, owner):

        try:
            item = RecycleBinItem.objects.get(
                id=item_id,
                owner=owner
            )

            item_name = item.item_name

            item.delete()

            HistoryService.log_command(
                owner,
                f"permanent delete {item_name}"
            )

            LogService.create_log(
                "PERMANENT_DELETE",
                f"Permanently deleted: {item_name}",
                owner
            )

            return True

        except RecycleBinItem.DoesNotExist:
            return False