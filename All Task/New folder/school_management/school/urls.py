from django.urls import path
#from rest_framework_jwt.views import refresh_jwt_token
from .views import SchoolSignUpAPIView, StudentCreateAPIView, StudentListAPIView, StudentUpdateAPIView #SchoolJWTAPIView


urlpatterns = [
    path('signup/', SchoolSignUpAPIView.as_view(), name='school-signup'),
    path('students/', StudentCreateAPIView.as_view(), name='student-create'),
    path('students/list/', StudentListAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentUpdateAPIView.as_view(), name='student-update'),
    #path('token/', SchoolJWTAPIView.as_view(), name='school-jwt'),
    #path('grades/', GradeAPIView.as_view(), name='grade-list'),
    #path('token/refresh/', refresh_jwt_token),
]
