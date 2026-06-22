from django.test import TestCase
from django.contrib.auth.models import User

from logs_api.models import LogEntry


class LogEntryTests(TestCase):

    # =========================
    # LOG CREATION
    # =========================
    def test_create_log(self):

        user = User.objects.create_user(
            username="abhishek",
            password="test123"
        )

        log = LogEntry.objects.create(
            user=user,
            action="LOGIN",
            description="User logged in"
        )

        self.assertEqual(log.action, "LOGIN")
        self.assertEqual(log.user.username, "abhishek")

    # =========================
    # STRING REPRESENTATION
    # =========================
    def test_string_representation(self):

        user = User.objects.create_user(
            username="john",
            password="test123"
        )

        log = LogEntry.objects.create(
            user=user,
            action="CREATE_FILE"
        )

        self.assertEqual(
            str(log),
            "john - CREATE_FILE"
        )

    # =========================
    # TIMESTAMP CREATED
    # =========================
    def test_created_at_exists(self):

        user = User.objects.create_user(
            username="admin",
            password="test123"
        )

        log = LogEntry.objects.create(
            user=user,
            action="DELETE_FILE"
        )

        self.assertIsNotNone(log.created_at)

    # =========================
    # MULTIPLE LOGS
    # =========================
    def test_multiple_logs(self):

        user = User.objects.create_user(
            username="multiuser",
            password="test123"
        )

        LogEntry.objects.create(
            user=user,
            action="LOGIN"
        )

        LogEntry.objects.create(
            user=user,
            action="LOGOUT"
        )

        self.assertEqual(
            LogEntry.objects.filter(user=user).count(),
            2
        )

    # =========================
    # USER OWNERSHIP
    # =========================
    def test_logs_belong_to_correct_user(self):

        user1 = User.objects.create_user(
            username="user1",
            password="123"
        )

        user2 = User.objects.create_user(
            username="user2",
            password="123"
        )

        LogEntry.objects.create(
            user=user1,
            action="LOGIN"
        )

        LogEntry.objects.create(
            user=user2,
            action="LOGOUT"
        )

        self.assertEqual(
            LogEntry.objects.filter(user=user1).count(),
            1
        )

        self.assertEqual(
            LogEntry.objects.filter(user=user2).count(),
            1
        )