from django.shortcuts import render
from .serializer import BlogSerializer
from rest_framework import viewsets
from .models import Blog


# Create your views here.

class BlogView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class LoginView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
