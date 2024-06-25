from django.urls import path
from socialmedia.views import *
from socialmedia.api_view import *
from . import api_view
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
path('login/',TokenObtainPairView.as_view(),name='token_obtain'),
path('refresh/',TokenRefreshView.as_view(),name='token_refresh'),
path('signup/',api_view.register,name='signup')

]