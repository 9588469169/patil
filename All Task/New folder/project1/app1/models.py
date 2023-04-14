from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class SchoolManager(BaseUserManager):
    def create_user(self, email, name, city, pin_code, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            city=city,
            pin_code=pin_code
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, city, pin_code, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            city=city,
            pin_code=pin_code,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class School(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=6)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = SchoolManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'city', 'pin_code']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Student(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    grade = models.IntegerField()

    def __str__(self):
        return self.username

