from django.db import models
# from api.settings import AUTH_USER_MODEL

# Create your models here.
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    content = models.TextField()

    def __str__(self):
        return self.title
