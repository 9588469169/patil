from django.contrib import admin
from .models import School,Student

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display=['id','email','name','city','pin_code','password'

    ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['school','name','username','password','grade'
        
    ]