from django.test import TestCase
from django.contrib.auth.models import User

from users_api.models import UserProfile


class UserProfileTests(TestCase):

    # =========================
    # USER CREATION
    # =========================
    def test_create_user(self):

        user = User.objects.create_user(
            username="abhishek",
            password="test123"
        )

        self.assertEqual(user.username, "abhishek")

    # =========================
    # PROFILE CREATION
    # =========================
    def test_create_profile(self):

        user = User.objects.create_user(
            username="john",
            password="test123"
        )

        # Profile is automatically created by signal
        profile = user.profile

        self.assertEqual(profile.user.username, "john")
        self.assertEqual(profile.role, "USER")

    # =========================
    # ADMIN ROLE
    # =========================
    def test_admin_role(self):

        user = User.objects.create_user(
            username="admin",
            password="admin123"
        )

        profile = user.profile
        profile.role = "ADMIN"
        profile.save()

        self.assertEqual(profile.role, "ADMIN")

    # =========================
    # DEFAULT ROLE
    # =========================
    def test_default_role(self):

        user = User.objects.create_user(
            username="normaluser",
            password="test123"
        )

        profile = user.profile

        self.assertEqual(profile.role, "USER")

    # =========================
    # USER AUTHENTICATION
    # =========================
    def test_user_password_check(self):

        user = User.objects.create_user(
            username="secureuser",
            password="mypassword"
        )

        self.assertTrue(
            user.check_password("mypassword")
        )

        self.assertFalse(
            user.check_password("wrongpassword")
        )