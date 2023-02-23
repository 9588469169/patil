from django.urls import path
from .import views

urlpatterns = [
    path('User/', views.users_create, name = 'user'),
    path('show_user/', views.show_data, name='show_user'),
    path('Create_department/',views.create_department, name='create_department'),
    path('Assign_department/<int:pk>/', views.assign_department,name = 'assing_department'),
    path('Departments_list/', views.departments_list,name = 'departments_list'),
    path('Update_department/<int:pk>/', views.update_department,name = 'update_department'),
    path('Delete_department/<int:pk>/', views.delete_department,name = 'delete_department'),
    path('Create_ticket/', views.create_ticket,name = 'create_ticket'),
    path('confirm_ticket_submission/', views.confirm_ticket_submission,name = 'confirm_ticket_submission'),
    path('delete_ticket/<int:pk>/', views.delete_ticket,name='delete_ticket'),
    path('update_ticket/<int:pk>/', views.update_ticket,name='update_ticket'),
    path('Manage_tickets/', views.manage_tickets,name = 'manage_tickets'),
]