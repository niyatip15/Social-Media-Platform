
from rest_framework import generics
from .models import Post
from posts.serializer import PostSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer