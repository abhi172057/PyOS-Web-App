from django.db import models
from django.contrib.auth.models import User


class Directory(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subdirectories'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    directory = models.ForeignKey(
        Directory,
        on_delete=models.CASCADE,
        related_name='files'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name