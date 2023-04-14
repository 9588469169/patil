from django.shortcuts import render, redirect,HttpResponse
from .models import Post
from .serializers import PostSerializer,SignUpSer
from rest_framework. response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import views,generics,permissions
from django.db.models import Q 
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models.signals import post_save
from django.dispatch import receiver



class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
    

#create post---------------------------------------------->>>>>>
class PostCreateView(generics.CreateAPIView):## add_data ---->>>CreateAPIView
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]


'''
    def perform_create(self, serializer):
        post = serializer.save(author=self.request.user)
        send_mail(
            'New post created',
            f'Your new post "{post.title}" has been created.',
            settings.DEFAULT_FROM_EMAIL,
            [self.request.user.email],
            fail_silently=False,
        )
'''

@receiver(post_save, sender=Post)
def send_post_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'New post created',
            f'Your new post "{instance.title}" has been created.',
            settings.DEFAULT_FROM_EMAIL,
            [instance.author.email],
            fail_silently=False,
        )


#if user is authenticated and isowner then read
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes=[JWTAuthentication]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(Q(author=self.request.user))
        

    #for the purpose of pagination--------->>>>>>>>>>
    class StandardResultsSetPagination(PageNumberPagination):
        page_size = 2
        page_size_query_param = 'page_size'
        max_page_size = 100

    pagination_class = StandardResultsSetPagination


#retrieve all records-------------------------------------->>
class PostListAllView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes=[JWTAuthentication] 

    #filter the records--------->>>>>>>
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title', 'body',]
    ordering_fields = ['id']
    ordering = ['-id']

    '''
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)
    '''
    
    class StandardResultsSetPagination(PageNumberPagination):
        page_size = 2
        page_size_query_param = 'page_size'
        max_page_size = 100

    pagination_class = StandardResultsSetPagination


## get_particular_record----------------------------------->> 
class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes=[JWTAuthentication]


# update & Partial update----------------------------------->>
class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# delete_record Their own records only------------------------------------->>
class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes=[JWTAuthentication]


#Fiter the record as per title , id, body and author------>>>>>>>>>>
class PostSearchList(PostListAllView):
    def get_queryset(self):
        queryset = super().get_queryset()
        title_query = self.request.query_params.get('title', None)
        id_query = self.request.query_params.get('id', None)
        body_query = self.request.query_params.get('body', None)
        author = self.request.query_params.get('author', None)
        if title_query is not None:
            queryset = queryset.filter(title__icontains=title_query)
        if id_query is not None:
            queryset = queryset.filter(id=id_query)
        if body_query is not None:
            queryset = queryset.filter(body__icontains=body_query)
        if author is not None:
            queryset = queryset.filter(author__icontains=author)
        return queryset



#Create User----------------------------------------->>>
class SignUpAPI(views.APIView):
    def post (self,request):
        ser = SignUpSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    


