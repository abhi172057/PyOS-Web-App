from django.db import models
from django.contrib.auth.models import User


class LogEntry(models.Model):

    ACTION_CHOICES = (
        ("LOGIN", "LOGIN"),
        ("LOGOUT", "LOGOUT"),
        ("CREATE_FILE", "CREATE_FILE"),
        ("DELETE_FILE", "DELETE_FILE"),
        ("MOVE_FILE", "MOVE_FILE"),
        ("CREATE_DIRECTORY", "CREATE_DIRECTORY"),
        ("DELETE_DIRECTORY", "DELETE_DIRECTORY"),
        ("ADD_USER", "ADD_USER"),
        ("DELETE_USER", "DELETE_USER"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="logs"
    )

    action = models.CharField(
        max_length=50,
        choices=ACTION_CHOICES
    )

    description = models.TextField(
        blank=True,
        default=""
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action}"