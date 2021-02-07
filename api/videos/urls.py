from django.urls import path

from .views import VideoListView, VideoDetailView, VideoCreateView

urlpatterns = [
    path('', VideoListView.as_view()),
    path('upload', VideoCreateView.as_view()),
    path('<pk>', VideoDetailView.as_view()),



]
