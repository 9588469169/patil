from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskModelSerializers(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields ='__all__'

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=10)
    class Meta:
        model =User
        fields =('username','password','email')
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
