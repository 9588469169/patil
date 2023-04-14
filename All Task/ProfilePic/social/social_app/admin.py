from django.contrib import admin
from .models import CustomUser


class CustomAdmin(admin.ModelAdmin):
    list_display = ['username','password', 'email', 'phone_no', 'address', 'city', 'state', 'country', 'profile_pic']

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info',{
            'fields':('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('phone_no', 'address', 'city', 'state', 'country', 'profile_pic')
        })
    )


    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('phone_no', 'address', 'city', 'state', 'country', 'profile_pic')
        })
    )
    

admin.site.register(CustomUser, CustomAdmin)


