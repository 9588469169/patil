from django.contrib import admin
from.models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display =[
        'id','name','phone_number','email','query','created_at'
    ]
