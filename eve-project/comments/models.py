from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from articles.models import Article

from videos.models import Video


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']


class ArticlesComment(Comment):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class VideosComment(Comment):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
