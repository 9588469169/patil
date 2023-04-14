from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import views


class SchoolSignUpAPIView(generics.CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    
class StudentCreateAPIView(generics.CreateAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class StudentListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['grade']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Student.objects.all()
        return Student.objects.filter(school=self.request.user)

class StudentUpdateAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

'''
class SchoolJWTAPIView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            school = School.objects.get(email=request.data['email'])
            response.data['is_staff'] = school.is_staff
        return response

'''