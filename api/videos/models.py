from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=300, default="")
    video_url = models.URLField(max_length=128)