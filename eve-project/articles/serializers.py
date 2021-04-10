from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
<<<<<<< HEAD
        fields = ('id', 'title', 'author', ' user_id', 'content')
=======
        fields = ('id', 'title', 'author', 'user_id', 'content')
>>>>>>> b3422c6b2aae7e0b55af53886d6ad3499308fb3d
