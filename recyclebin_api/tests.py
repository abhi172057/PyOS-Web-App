from django.test import TestCase
from django.contrib.auth.models import User

from filesystem_api.models import Directory, File
from recyclebin_api.models import RecycleBinItem
from recyclebin_api.services.recycle_service import RecycleService


class RecycleBinTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="abhishek",
            password="test123"
        )

        self.directory = Directory.objects.create(
            name="Documents",
            owner=self.user
        )

    # =========================
    # RECYCLE BIN ITEM CREATION
    # =========================
    def test_create_recycle_item(self):

        item = RecycleBinItem.objects.create(
            owner=self.user,
            item_name="test.txt",
            item_type="file",
            content="hello world"
        )

        self.assertEqual(item.item_name, "test.txt")
        self.assertEqual(item.item_type, "file")

    # =========================
    # GET BIN ITEMS
    # =========================
    def test_get_bin(self):

        RecycleBinItem.objects.create(
            owner=self.user,
            item_name="file1.txt",
            item_type="file"
        )

        items = RecycleService.get_bin(self.user)

        self.assertEqual(items.count(), 1)

    # =========================
    # RESTORE FILE
    # =========================
    def test_restore_file(self):

        item = RecycleBinItem.objects.create(
            owner=self.user,
            item_name="restore.txt",
            item_type="file",
            content="restored content",
            parent_id=self.directory.id
        )

        result = RecycleService.restore_item(
            item.id,
            self.user
        )

        self.assertTrue(result)

        self.assertTrue(
            File.objects.filter(
                name="restore.txt"
            ).exists()
        )

    # =========================
    # PERMANENT DELETE
    # =========================
    def test_permanent_delete(self):

        item = RecycleBinItem.objects.create(
            owner=self.user,
            item_name="delete.txt",
            item_type="file"
        )

        result = RecycleService.permanent_delete(
            item.id,
            self.user
        )

        self.assertTrue(result)

        self.assertFalse(
            RecycleBinItem.objects.filter(
                id=item.id
            ).exists()
        )

    # =========================
    # RESTORE NON EXISTING ITEM
    # =========================
    def test_restore_invalid_item(self):

        result = RecycleService.restore_item(
            9999,
            self.user
        )

        self.assertFalse(result)