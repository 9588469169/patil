from django.urls import path
from.import views

urlpatterns=[
    path('signup/', views.SignUpAPI.as_view(),name='Signup'),

    #path('like/', views.LikeListView.as_view()),
    #path('like1/',views.LikeCreateView.as_view()),
    #path('like/<int:pk>/', views.LikeRetrieveView.as_view()),
    #path('like_update/<int:pk>/', views.LikeUpdateView.as_view()),
    #path('like_delete/<int:pk>/', views.LikeDeleteView.as_view()),

    #path('post/', views.PostListView.as_view()),
    #path('post1/',views.PostCreateView.as_view()),
    #path('post/<int:pk>/', views.PostRetrieveView.as_view()),
    #path('post_update/<int:pk>/', views.PostUpdateView.as_view()),
    #path('post_delete/<int:pk>/', views.PostDeleteView.as_view()),

]