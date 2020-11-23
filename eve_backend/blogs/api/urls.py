from django.urls import path

from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view()),
    path('<pk>', BlogDetailView.as_view()),
]