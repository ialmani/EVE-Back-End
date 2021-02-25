from rest_framework import serializers

from .models import ArticlesComment


class ArticlesCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlesComment
        fields = ('id', 'article', 'user', 'body','created_on')
