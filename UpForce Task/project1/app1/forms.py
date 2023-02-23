from django import forms
from.models import Post,Like

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields ='__all__'

class LikeForm(forms.ModelForm):
    class Meta:
        model =Like
        fields ='__all__'