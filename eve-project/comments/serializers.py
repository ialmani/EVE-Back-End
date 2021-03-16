from rest_framework import serializers

from .models import ArticlesComment, Comment


class Comment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'body','created_on')

class ArticlesCommentSerializer(Comment):
    class Meta:
        model = ArticlesComment
        fields = ('id', 'article', 'user', 'body','created_on')


class VideosCommentSerializer(Comment):
    class Meta:
        model = ArticlesComment
        fields = ('id', 'video', 'user', 'body','created_on')