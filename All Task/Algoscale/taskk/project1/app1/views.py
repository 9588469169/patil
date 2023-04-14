from django.shortcuts import render
from.models import Task
from.serializers import TaskModelSerializers,SignUpSerializer
from rest_framework import viewsets,views
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class SignUpSerializersView(views.APIView):
    def post(self,request):
        ser = SignUpSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)