from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from web.models import Post
from web.serializers import PostSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    