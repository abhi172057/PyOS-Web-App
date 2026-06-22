from django.db import models
from django.contrib.auth.models import User


class RecycleBinItem(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recycle_bin"
    )

    item_name = models.CharField(max_length=255)

    item_type = models.CharField(max_length=20)  # file / directory

    original_id = models.IntegerField(null=True, blank=True)

    parent_id = models.IntegerField(null=True, blank=True)

    content = models.TextField(blank=True, default="")

    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} ({self.item_type})"