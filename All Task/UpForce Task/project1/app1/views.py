from django.shortcuts import render, redirect,HttpResponse
from .models import Post, Like
from .serializers import PostSerializer,LikeSerializer,SignUpSer
from rest_framework. response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import views,generics,viewsets,permissions
from django.db.models import Q 
from rest_framework.response import Response


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

## USING MODEL VIWESET----->>>
class LikeListView(viewsets.ModelViewSet):##Perform All actions--->>> 
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]


class PostListView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly,permissions.IsAuthenticatedOrReadOnly]
    authentication_classes=[JWTAuthentication]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(Q(owner=self.request.user)|Q(is_public=True))
        else:
            return Post.objects.filter(is_public=True)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = serializer.data
        for blog in response_data:
            blog["likes_count"] = blog.pop("likes_count")
        return Response(response_data)


'''
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(Q(owner=self.request.user)|Q(is_public=True))
        else:
            return Post.objects.filter(is_public=True)
'''
'''
### USING Genereic ViewSet--->>>

class LikeListView(generics.ListAPIView):##get_all_data--->>>> ListAPIView 
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class LikeCreateView(generics.CreateAPIView):## add_data ---->>>CreateAPIView
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class LikeRetrieveView(generics.RetrieveAPIView):## get_particular_record-->>RetrieveAPIView
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class LikeUpdateView(generics.UpdateAPIView):## get_update_record-->>UpdateAPIView
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]

class LikeDeleteView(generics.DestroyAPIView):# delete_record-->>DestroyAPIView
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]



    
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes=[JWTAuthentication]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(Q(owner=self.request.user)|Q(is_public=True))
        else:
            return Post.objects.filter(is_public=True)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = serializer.data
        for blog in response_data:
            blog["likes_count"] = blog.pop("likes_count")
        return Response(response_data)

class PostCreateView(generics.CreateAPIView):## add_data ---->>>CreateAPIView
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    
class PostRetrieveView(generics.RetrieveAPIView):## get_particular_record-->>RetrieveAPIView
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes=[JWTAuthentication]


    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(Q(owner=self.request.user)|Q(is_public=True))
        else:
            return Post.objects.filter(is_public=True)
        

class PostUpdateView(generics.UpdateAPIView):## get_update_record-->>UpdateAPIView
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes=[JWTAuthentication]
    

class PostDeleteView(generics.DestroyAPIView):# delete_record-->>DestroyAPIView
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes=[JWTAuthentication]


'''
class SignUpAPI(views.APIView):
    def post (self,request):
        ser = SignUpSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
