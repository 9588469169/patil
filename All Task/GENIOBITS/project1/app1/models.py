from django.db import models

class User(models.Model):
    name =models.CharField(max_length=50)
    address = models.TextField()
    qualifications = models.CharField(max_length=50)


class JobListing(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.FloatField()
    # Add other fields as needed

    def __str__(self) -> str:
        return f'{self.title}'
    
class JobApplication(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    # Add other fields as needed
    def __str__(self) -> str:
        return f'{self.job_listing}'

class JobApplication(models.Model):
    JOB_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    )

    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=JOB_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)