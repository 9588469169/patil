from django.contrib import admin
from .models import Product,User

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['id','user','name','description','price','created_at','updated_at']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name','email' ,'mobile','password']