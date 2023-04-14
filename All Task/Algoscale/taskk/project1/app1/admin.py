from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class AdminModel(admin.ModelAdmin):
    list_display = ['task','desc','due_date','status']