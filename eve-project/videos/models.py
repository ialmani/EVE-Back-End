from django.db import models
from api.settings import AUTH_USER_MODEL

class Video(models.Model):
    title = models.CharField(max_length=120)
    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='video')
    description = models.TextField(max_length=300, default="")
    video_url = models.URLField(max_length=128)