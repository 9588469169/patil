from django.db import models

Choice_field=(['Completed','Completed'],['Pending','Pending'])
class Task(models.Model):
    task=models.CharField(max_length=50)
    desc = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=50,choices=Choice_field)