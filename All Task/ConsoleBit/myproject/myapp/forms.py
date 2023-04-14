from django import forms
from.models import Product,User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields ='__all__'
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields ='__all__'