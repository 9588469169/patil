from django.shortcuts import render, redirect,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import Enquiry
from .forms import EnquiryForm
from datetime import datetime, timedelta
import time
from django.conf import settings
from celery import shared_task
from django.urls import reverse

def enquiry_view(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()
            review_url = f'http://127.0.0.1:8000/project/feedback/{enquiry.id}/'
            send_mail(
                'New Enquiry from Customer',
                f'A new enquiry has been submitted by \nName:{enquiry.name}\nPhone number: {enquiry.phone_number}\nEmail: {enquiry.email}\nQuery: {enquiry.query} \nYour Id:{enquiry.id} \n\nurl:{review_url}',
                settings.DEFAULT_FROM_EMAIL,
                ['gp.smtp1234@gmail.com'],
                fail_silently=False,
            )
            if request.method == 'POST':
                res = redirect('enquiry_success')
                send_review_email(request, enquiry.id)
                return (res)
    return render(request, 'enquiry/enquiry.html', {'form': form})

def enquiry_success_view(request):
    return render(request, 'enquiry/enquiry_success.html')

def send_review_email(request,enquiry_id):
    enquiry = Enquiry.objects.get(id=enquiry_id)
    now = timezone.now()
    expiry_time = now + timezone.timedelta(minutes=5)
    expiry_time_url = expiry_time.strftime('%Y-%m-%d %H:%M:%S')
    review_url = request.build_absolute_uri(reverse('review', args=[enquiry_id]))
    #review_url = f'http://127.0.0.1:8000/project/review/{enquiry_id}/'
    email_body = f'Please provide your satisfaction feedback for your enquiry. The link will expire at {expiry_time_url}. {review_url}'
    email_subject = 'Customer Satisfaction Review'
    time.sleep(120)
    send_mail(email_subject, email_body, settings.DEFAULT_FROM_EMAIL, [enquiry.email], fail_silently=False)
    return HttpResponse('Email Sended.....!!!')


def review_view(request, enquiry_id):
    enquiry = Enquiry.objects.get(id=enquiry_id)
    now = timezone.now()
    expiry_time = enquiry.created_at + timezone.timedelta(minutes=5)
    print(now,'------Start Time------')
    print(expiry_time,'-----Expire Time-----')
    if now >= expiry_time:
        return HttpResponse('The URL has expired')
    if request.method == 'POST':
        satisfaction = request.POST.get('satisfaction')
        enquiry.satisfaction = satisfaction
        enquiry.save()
        return redirect('feedback_success')
    return render(request, 'enquiry/review.html', {'enquiry': enquiry})

def feedback_view(request, enquiry_id):
    enquiry = Enquiry.objects.get(id=enquiry_id)
    if request.method == 'POST':
        enquiry.response = request.POST['response']
        enquiry.response_date = timezone.now()
        enquiry.save()
        send_mail(
            'Enquiry Response',
            f'Your enquiry has been responded to:\n\nName: {enquiry.name}\nPhone number: {enquiry.phone_number}\nEmail: {enquiry.email}\nQuery: {enquiry.query}\n\nResponse:\n\n{enquiry.response}\n\nResponse Date:{enquiry.response_date}',
            settings.DEFAULT_FROM_EMAIL,
            [enquiry.email],
            fail_silently=False,
        )
        return redirect('feedback_success')
    review_view(request, enquiry_id)
    return render(request, 'enquiry/feedback.html', {'enquiry': enquiry})

def feedback_success_view(request):
    return render(request, 'enquiry/feedback_success.html')