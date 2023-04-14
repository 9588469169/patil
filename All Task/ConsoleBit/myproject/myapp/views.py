from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product
from .serializers import ProduceSerializers,SignUpSerializer
from rest_framework.response import Response
from rest_framework import views
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .forms import ProductForm,UserForm
from django.shortcuts import render,redirect,HttpResponse
from django.db.models import Q

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProduceSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    # pagination code
    class StandardResultsSetPagination(PageNumberPagination):
        page_size = 1
        page_size_query_param = 'page_size'
        max_page_size = 100

    pagination_class = StandardResultsSetPagination

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProduceSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


#for filter by id,name,price,description----------------------->>>>>
class ProductSearchList(ProductList):
    def get_queryset(self):
        queryset = super().get_queryset()
        name_query = self.request.query_params.get('name', None)
        id_query = self.request.query_params.get('id', None)
        description_query = self.request.query_params.get('description', None)
        query = self.request.query_params.get('query', None)
        if name_query is not None:
            queryset = queryset.filter(name__icontains=name_query)
        if id_query is not None:
            queryset = queryset.filter(id=id_query)
        if description_query is not None:
            queryset = queryset.filter(name__icontains=description_query)
        if query is not None:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query))
        min_price = self.request.query_params.get('min_price', None)
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        max_price = self.request.query_params.get('max_price', None)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
        price = self.request.query_params.get('price', None)
        if price is not None:
            queryset = queryset.filter(price=price)
        return queryset


class ProductOrdering(generics.ListAPIView):
    serializer_class = ProduceSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'price', 'created_at']
    ordering = ['price']
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

class SignUpAPI(views.APIView):
    def post (self,request):
        ser = SignUpSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
