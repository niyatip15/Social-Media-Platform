from rest_framework import serializers
from socialmedia.serializer import UserSerializer
from posts.models import *

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    created_at_formatted_date = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'content', 'created_by', 'created_at_formatted_date', 'created_at')

    def get_created_at_formatted_date(self, obj):
        return timesince(obj.created_at)