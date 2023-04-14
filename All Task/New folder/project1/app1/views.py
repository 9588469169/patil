from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer, StudentBulkSerializer, StudentUpdateSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class SchoolSignup(APIView):
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentBulkCreate(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes =[JWTAuthentication]

    def post(self, request, grade):
        serializer = StudentBulkSerializer(data=request.data)
        if serializer.is_valid():
            students = serializer.save()
            for student in students:
                student.grade = grade
                student.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes =[JWTAuthentication]

    def get(self, request, grade):
        students = Student.objects.filter(grade=grade)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class StudentUpdate(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes =[JWTAuthentication]

    def put(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        self.check_object_permissions(request, student)
        serializer = StudentUpdateSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
