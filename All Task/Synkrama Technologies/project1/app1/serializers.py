from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author']

    
class SignUpSer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ('username','password', 'email')

    def create(self,validate_data):
        return User.objects.create_user(**validate_data)