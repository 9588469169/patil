from django.db import models

class School(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    grade = models.IntegerField()
    