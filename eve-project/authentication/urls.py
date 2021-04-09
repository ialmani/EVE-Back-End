from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi, UserApi
from .views import UserDetailView
urlpatterns = [
    path('api/register', RegisterApi.as_view()),
    path('api/get_current_user', UserApi.as_view()),
    path('users/<pk>', UserDetailView.as_view())
]