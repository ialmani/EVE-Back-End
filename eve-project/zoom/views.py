from django.shortcuts import render

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
from .models import Zoom
from .serializers import ZoomSerializer

class ZoomListView(ListAPIView):
    queryset = Zoom.objects.all()
    serializer_class = ZoomSerializer
    permission_classes = (permissions.AllowAny,)


class ZoomDetailView(RetrieveAPIView):
    queryset = Zoom.objects.all()
    serializer_class = ZoomSerializer
    permission_classes = (permissions.AllowAny,)


class ZoomCreateView(CreateAPIView):
    queryset = Zoom.objects.all()
    serializer_class = ZoomSerializer
    permission_classes = (permissions.AllowAny,)


class ZoomUpdateView(UpdateAPIView):
    queryset = Zoom.objects.all()
    serializer_class = ZoomSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ZoomDeleteView(DestroyAPIView):
    queryset = Zoom.objects.all()
    serializer_class = ZoomSerializer
    permission_classes = (permissions.IsAuthenticated,)

