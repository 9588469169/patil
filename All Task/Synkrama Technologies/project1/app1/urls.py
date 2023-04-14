from django.urls import path
from.import views

urlpatterns=[
    #signup url---->>>>
    path('signup/', views.SignUpAPI.as_view(),name='Signup'),

    path('POST/api/posts/',views.PostCreateView.as_view()),
    path('GET/api/posts/', views.PostListView.as_view()),
    path('GET/api/posts/<int:pk>/', views.PostRetrieveView.as_view()),
    path('GET/api/posts/all/',views.PostListAllView.as_view()),
    path('PUT/api/posts/<int:pk>/', views.PostUpdateView.as_view()),
    path('DELETE/api/posts/<int:pk>/', views.PostDeleteView.as_view()),
    path('GET/api/posts/search/', views.PostSearchList.as_view(), name='post-search'),

]


#filter------->>
#http://127.0.0.1:8000/project1/GET/api/posts/search/?body=mmm

#Order by ID------>>Reverse
#http://127.0.0.1:8000/project1/GET /api/posts/all/?ordering=-id