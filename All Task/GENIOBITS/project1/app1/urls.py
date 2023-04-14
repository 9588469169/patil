from django.urls import path
from.import views

urlpatterns=[
    path('create_job_listing/',views.create_job_listing, name='create_job_listing'),
    path('apply_for_job/<int:pk>/', views.apply_for_job, name='apply_for_job'),
    path('all_jobs/', views.all_job, name='all_jobs'),
    path('update_jobs/<int:pk>/', views.update_jobs, name='update_jobs'),
    path('delete_jobs/<int:pk>/', views.delete_jobs, name='delete_jobs'),

]
