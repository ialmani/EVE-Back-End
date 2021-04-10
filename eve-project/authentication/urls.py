from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi, UserApi
from .views import UserDetailView
urlpatterns = [
    path('users/<pk>', UserDetailView.as_view())
]