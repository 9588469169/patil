from django.contrib import admin
from .models import User,Department,Ticket


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','department','role']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','created_by','created_at','last_updated_at']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id','user','subject','body','priority','email','phone_number']