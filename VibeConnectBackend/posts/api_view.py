
from rest_framework import generics
from .models import Post
from rest_framework.permissions import AllowAny
from posts.serializer import PostSerializer

class PostListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny] 
    queryset = Post.objects.all()
    serializer_class = PostSerializer