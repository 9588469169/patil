from rest_framework import serializers
from .models import School,Student

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['email', 'name', 'username','city', 'pin_code', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'username', 'password', 'grade']
        extra_kwargs = {'password': {'write_only': True}}

