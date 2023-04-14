from django.urls import path
from .views import *

urlpatterns=[
    path('signup/',SignUpSerializersView.as_view(), name='signup')
]