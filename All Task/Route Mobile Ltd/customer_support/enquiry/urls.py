from django.urls import path
from . import views

urlpatterns = [
    path('enquiry/', views.enquiry_view, name='enquiry'),
    path('success/', views.enquiry_success_view, name='enquiry_success'),
    path('feedback/<int:enquiry_id>/', views.feedback_view, name='feedback'),
    path('feedback/success/', views.feedback_success_view, name='feedback_success'),
    path('review/send_review_email/<int:enquiry_id>/',views.send_review_email,name='send_review_email'),
    path('review/<int:enquiry_id>/', views.review_view, name='review'),
]
