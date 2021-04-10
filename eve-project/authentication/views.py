from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.conf.global_settings import AUTH_USER_MODEL




class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        user_id = self.kwargs['pk']
        return AUTH_USER_MODEL.objects.filter(id=user_id)
