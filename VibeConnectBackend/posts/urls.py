from django.urls import path
from posts.api_view import *

urlpatterns = [
    path('',PostListAPIView.as_view(), name='posts')
]