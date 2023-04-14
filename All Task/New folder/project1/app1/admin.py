from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import School, Student


class SchoolAdmin(UserAdmin):
    list_display = ('id','email', 'name', 'city', 'pin_code', 'is_active', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'city', 'pin_code')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'city', 'pin_code', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'name', 'city', 'pin_code')
    ordering = ('email',)
    filter_horizontal = ()


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'username', 'password', 'grade')
    list_filter = ('grade',)



admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
