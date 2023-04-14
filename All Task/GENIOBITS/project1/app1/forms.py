from django import forms
from .models import JobListing, JobApplication

class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['title', 'location', 'salary' ]


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['resume', 'cover_letter']
