from rest_framework import serializers
from .models import Post, Like
from django.contrib.auth.models import User


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user']

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'owner', 'is_public', 'likes_count']

    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
class SignUpSer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)
    class Meta:
        model = User
        fields = ('username','password', 'email')

    def create(self,validate_data):
        return User.objects.create_user(**validate_data)