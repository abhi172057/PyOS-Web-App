from django.test import TestCase
from django.contrib.auth.models import User

from filesystem_api.models import Directory, File


class FileSystemModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="test123"
        )

    # =========================
    # DIRECTORY CREATION
    # =========================
    def test_create_directory(self):

        directory = Directory.objects.create(
            name="Documents",
            owner=self.user
        )

        self.assertEqual(directory.name, "Documents")
        self.assertEqual(directory.owner, self.user)

    # =========================
    # SUB DIRECTORY CREATION
    # =========================
    def test_create_subdirectory(self):

        parent = Directory.objects.create(
            name="Root",
            owner=self.user
        )

        child = Directory.objects.create(
            name="Child",
            owner=self.user,
            parent=parent
        )

        self.assertEqual(child.parent, parent)

    # =========================
    # FILE CREATION
    # =========================
    def test_create_file(self):

        directory = Directory.objects.create(
            name="Docs",
            owner=self.user
        )

        file = File.objects.create(
            name="notes.txt",
            content="Hello World",
            owner=self.user,
            directory=directory
        )

        self.assertEqual(file.name, "notes.txt")
        self.assertEqual(file.directory, directory)
        self.assertEqual(file.owner, self.user)

    # =========================
    # DIRECTORY FILE RELATION
    # =========================
    def test_directory_contains_files(self):

        directory = Directory.objects.create(
            name="Docs",
            owner=self.user
        )

        File.objects.create(
            name="file1.txt",
            owner=self.user,
            directory=directory
        )

        File.objects.create(
            name="file2.txt",
            owner=self.user,
            directory=directory
        )

        self.assertEqual(directory.files.count(), 2)

    # =========================
    # USER OWNERSHIP
    # =========================
    def test_file_owner(self):

        directory = Directory.objects.create(
            name="Docs",
            owner=self.user
        )

        file = File.objects.create(
            name="secret.txt",
            owner=self.user,
            directory=directory
        )

        self.assertEqual(file.owner.username, "testuser")