from django.db import models
from django.contrib.auth.models import User


class CommandHistory(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="command_history"
    )

    command = models.TextField()

    executed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.command}"