from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = School
        fields = ('id', 'email', 'name', 'city', 'pin_code', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        school = School.objects.create_user( **validated_data
        )
        return school


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'username', 'password', 'grade')


class StudentBulkSerializer(serializers.Serializer):
    students = StudentSerializer(many=True)

    def create(self, validated_data):
        students_data = validated_data['students']
        students = [Student(**student_data) for student_data in students_data]
        return Student.objects.bulk_create(students)


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'password')
