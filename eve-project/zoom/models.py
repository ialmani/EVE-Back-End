from django.db import models


class Zoom(models.Model):
    title = models.CharField(max_length=120)
    start_date = models.DateTimeField(max_length=300)
    end_date = models.DateTimeField(max_length=300)
    description = models.TextField(max_length=300, default="", blank=True)
    zoom_url = models.URLField()
    zoom_id = models.TextField(max_length=120)
    password = models.CharField(max_length=120, default="", blank=True)
