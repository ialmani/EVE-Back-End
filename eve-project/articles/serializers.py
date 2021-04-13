from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
<<<<<<< HEAD
        fields = ('id', 'title', 'author', ' user_id', 'content')
=======
        fields = ('id', 'title', 'author', 'user_id', 'content')
>>>>>>> 0b24e41d4ef388d915b34a14bf252ed75ece6473
