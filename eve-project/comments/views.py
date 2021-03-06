from django.shortcuts import render

from rest_framework import viewsets

from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from .models import ArticlesComment
from .serializers import ArticlesCommentSerializer

from django.apps import apps
Article = apps.get_model('articles', 'Article')


class ArticlesCommentListView(ListAPIView):
    serializer_class = ArticlesCommentSerializer
    permission_classes = (permissions.AllowAny,)
    def get_queryset(self):
        article_id = self.kwargs['pk']
        return ArticlesComment.objects.filter(article__id=article_id)

class ArticlesCommentDetailView(RetrieveAPIView):
    queryset = ArticlesComment.objects.all()
    serializer_class = ArticlesCommentSerializer
    permission_classes = (permissions.AllowAny,)


class ArticlesCommentCreateView(CreateAPIView):
    queryset = ArticlesComment.objects.all()
    serializer_class = ArticlesCommentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ArticlesCommentUpdateView(UpdateAPIView):
    queryset = ArticlesComment.objects.all()
    serializer_class = ArticlesCommentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ArticlesCommentDeleteView(DestroyAPIView):
    queryset = ArticlesComment.objects.all()
    serializer_class = ArticlesCommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

