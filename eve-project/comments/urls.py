from django.urls import path

from .views import ArticlesCommentListView, ArticlesCommentDetailView, ArticlesCommentCreateView

urlpatterns = [
    path('', ArticlesCommentListView.as_view()),
    path('create', ArticlesCommentCreateView.as_view()),
    path('<comment_id>', ArticlesCommentDetailView.as_view()),



]
