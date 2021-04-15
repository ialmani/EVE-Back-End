from django.db import models

from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=120)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video')
    description = models.TextField(max_length=300, default="")
    video_url = models.URLField(max_length=128)