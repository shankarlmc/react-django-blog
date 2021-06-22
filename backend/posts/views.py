from django.contrib.auth.models import User
from .permissions import (
    IsAuthorOrReadOnly,
    IsSuperUserOrReadOnly,
)
from .serializers import (
    PostSerializer,
    UserSerializer,
)
from django.shortcuts import render
from rest_framework import generics
from.models import Post
# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUserOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
