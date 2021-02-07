from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=120)
    video_url = models.URLField(max_length=128)