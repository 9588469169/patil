from django.contrib import admin
from.models import User,Post,Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=[
        'id','title','content','owner','is_public'
    ]

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=[
        'id','post','user'
    ]
