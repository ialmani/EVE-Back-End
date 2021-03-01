from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi, UserApi
urlpatterns = [
    path('api/register', RegisterApi.as_view()),
    path('api/getUserDetails', UserApi.as_view()),
]