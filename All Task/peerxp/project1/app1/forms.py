from .models import User,Ticket,Department
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields ='__all__'
'''
        labels={
            'name':'User Name',
            'email': 'Email ID',
            'phone_number': 'Phone Number',
            'password':'Password',
            'department': 'Department',
            'role': 'User Role',
            'created_by':'Created BY',
            }

        widgets ={
            'name':forms.TextInput(attrs={'class':'input-group-text','placeholder':'User Name'}),
            'email':forms.EmailInput(attrs={'class':'input-group-text','placeholder':'User Name'}),
            'phone_number':forms.NumberInput(attrs={'class':'input-group-text','placeholder':'User Name'}),
            'password':forms.NumberInput(attrs={'class':'input-group-text','placeholder':'User Name'}),
            'department':forms.TextInput(attrs={'class':'input-group-text','placeholder':'User Name'}),
            'role':forms.TextInput(attrs={'class':'input-group-text','placeholder':'User Name'}),
            'created_by':forms.TextInput(attrs={'class':'input-group-text','placeholder':'User Name'}),
    }

'''
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields ='__all__'


class NewTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['id','user','subject', 'body', 'priority', 'email', 'phone_number']
        widgets = {
            'email': forms.HiddenInput(),
            'phone_number': forms.HiddenInput(),
        }
