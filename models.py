from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_ops_user = models.BooleanField(default=False)
    is_client_user = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class File(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

class DownloadLink(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.link
