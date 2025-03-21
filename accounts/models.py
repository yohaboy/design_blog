from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser

class UserManager(BaseUserManager):

    def create_user(self, username, email,password=None ,**kwargs):
        if not email:
            raise ValueError('please enter your email')
        email = self.normalize_email(email)
        user = self.model(username = username , email = email ,**kwargs)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        return self.create_user(username, email, password, **kwargs)


class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    profile = models.FileField(upload_to="profiles/", blank=True, null=True ,default='profiles/Screenshot_from_2024-11-10_23-11-42.png')

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()