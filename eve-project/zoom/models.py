from django.db import models

class Zoom(models.Model):
    title = models.CharField(max_length=120)
    start_time = models.TextField(max_length=300, default="")
    date = models.DateField()
    description = models.TextField(max_length=300, default="")
    zoom_url = models.URLField(max_length=50)
    zoom_id = models.TextField(max_length=11, default="")
    password = models.CharField(max_length=120)