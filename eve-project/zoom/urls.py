from django.urls import path

from .views import ZoomListView, ZoomDetailView, ZoomCreateView

urlpatterns = [
    path('', ZoomListView.as_view()),
    path('create', ZoomCreateView.as_view()),
    path('<pk>', ZoomDetailView.as_view()),



]
