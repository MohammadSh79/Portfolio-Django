from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        return self.create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username__iexact=username)

class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True, blank=False, null=False)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=False, null=False)
    avatar = models.ImageField(upload_to='avatars/', blank=False, null=False, default='avatars/default.png')
    aboutme = models.TextField(max_length=300, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'