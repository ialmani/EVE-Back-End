from django.shortcuts import render

from .serializers import BlogSerializer
from django.shortcuts import render
from rest_framework import viewsets  # add this
from .models import Blog


# Create your views here.

class BlogView(viewsets.ModelViewSet):  # add this
    serializer_class = BlogSerializer  # add this
    queryset = Blog.objects.all()  # add this
