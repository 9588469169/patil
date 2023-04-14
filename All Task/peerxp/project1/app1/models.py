from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager



class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name}'

class UserManager(models.Model):
    def create_user(self, email, phone_number, password=None):
        if not email and not phone_number:
            raise ValueError('Users must have either an email or phone number')
        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            phone_number=phone_number,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        verbose_name='phone number',
        max_length=10,
        unique=True,
        null=True,
        blank=True,
    )
    password = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return f'{self.name}'

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    priority = models.CharField(choices=PRIORITY_CHOICES,max_length=50)
    email = models.EmailField(auto_created=True,blank=True)
    phone_number = models.CharField(max_length=15,auto_created=True,blank=True)


    def __str__(self):
        return f'{self.user}'


'''
class User(AbstractBaseUser):
    name= models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        verbose_name='phone number',
        max_length=10,
        unique=True,
        null=True,
        blank=True,
    )
    department= models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    #objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser



'''
'''
class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None):
        if not email and not phone_number:
            raise ValueError('Users must have either an email or phone number')
        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            phone_number=phone_number,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(models.Model):
    name= models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        verbose_name='phone number',
        max_length=10,
        unique=True,
        null=True,
        blank=True,
    )
    department= models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class User(AbstractBaseUser):
    name= models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        verbose_name='phone number',
        max_length=10,
        unique=True,
        null=True,
        blank=True,
    )
    department= models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class UserRole(models.Model):
    ADMIN = 1
    USER = 2
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=USER)

class Department(models.Model):
    subject = models.CharField(max_length=50)
    body = models.TextField()
    priority = models.CharField(max_length=50)
'''