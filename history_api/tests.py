from django.test import TestCase
from django.contrib.auth.models import User

from history_api.models import CommandHistory


class CommandHistoryTests(TestCase):

    # =========================
    # HISTORY CREATION
    # =========================
    def test_create_command_history(self):

        user = User.objects.create_user(
            username="abhishek",
            password="test123"
        )

        history = CommandHistory.objects.create(
            user=user,
            command="mkdir docs"
        )

        self.assertEqual(history.command, "mkdir docs")
        self.assertEqual(history.user.username, "abhishek")

    # =========================
    # MULTIPLE COMMANDS
    # =========================
    def test_multiple_commands(self):

        user = User.objects.create_user(
            username="john",
            password="test123"
        )

        CommandHistory.objects.create(
            user=user,
            command="mkdir test"
        )

        CommandHistory.objects.create(
            user=user,
            command="touch file.txt"
        )

        self.assertEqual(
            CommandHistory.objects.filter(user=user).count(),
            2
        )

    # =========================
    # STRING REPRESENTATION
    # =========================
    def test_string_representation(self):

        user = User.objects.create_user(
            username="admin",
            password="test123"
        )

        history = CommandHistory.objects.create(
            user=user,
            command="ls"
        )

        self.assertEqual(
            str(history),
            "admin: ls"
        )

    # =========================
    # EXECUTED_AT CREATED
    # =========================
    def test_timestamp_created(self):

        user = User.objects.create_user(
            username="timeuser",
            password="test123"
        )

        history = CommandHistory.objects.create(
            user=user,
            command="pwd"
        )

        self.assertIsNotNone(
            history.executed_at
        )

    # =========================
    # HISTORY BELONGS TO USER
    # =========================
    def test_history_owner(self):

        user1 = User.objects.create_user(
            username="user1",
            password="123"
        )

        user2 = User.objects.create_user(
            username="user2",
            password="123"
        )

        CommandHistory.objects.create(
            user=user1,
            command="mkdir docs"
        )

        CommandHistory.objects.create(
            user=user2,
            command="touch file.txt"
        )

        self.assertEqual(
            CommandHistory.objects.filter(user=user1).count(),
            1
        )

        self.assertEqual(
            CommandHistory.objects.filter(user=user2).count(),
            1
        )