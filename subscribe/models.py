import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager, BaseUserManager
from datetime import datetime

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     first_name = models.CharField(max_length=150, null=True, blank=True)
#     last_name = models.CharField(max_length=200, null=True, blank=True)
#     email = models.EmailField(max_length=255, unique=True)
#     mobile_no = models.CharField(max_length=130, null=True, blank=True)
#     company = models.TextField(default='NOT SPECIFIED')
#     username = models.CharField(max_length=20, null=True, blank=True)
#     USERNAME_FIELD = 'email'

#     objects = CustomUserManager()
#     is_staff = models.BooleanField(default=False, help_text=(
#         'Designates whether the user can log into this admin site.'))
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     is_customer = models.BooleanField(default=False)
#     customer_id = models.IntegerField(blank=True, null=True)
#     password_reset_salt = models.IntegerField(blank=True, null=True)

#     def get_full_name(self):
#         full_name = "%s %s" % (self.first_name, self.last_name)
#         return full_name or self.username or self.email

#     def get_short_name(self):
#         """Return the email."""
#         return self.email or self.username

#     def __str__(self):
#         return self.email  # self.username or self.first_name or self.last_name or self.email

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True,)
    first_name = models.CharField(max_length=30,blank=True,null=True)
    last_name = models.CharField(max_length=30,blank=True,null=True)
    # gender = models.CharField(
    #     max_length=10, choices=gender_choices, default='male')
    mobile_no = models.CharField(max_length=130, null=True, blank=True)
    company = models.TextField(default='NOT SPECIFIED')
    date_joined = models.DateTimeField('date joined', default=datetime.now)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    customer_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    objects = UserManager()
    password_reset_salt = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_short_name(self):
        "Returns the short name for the user."
        return self.email or self.username

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name or self.username or self.email