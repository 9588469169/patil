from django.contrib import admin
from.models import JobApplication,JobListing,User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','address','qualifications']


@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display=['title','location','salary']


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display=['job_listing','resume','cover_letter']