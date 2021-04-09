from django.db import models
from api.settings import AUTH_USER_MODEL

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='article')
    content = models.TextField()

    def __str__(self):
        return self.title
