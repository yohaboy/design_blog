from django.db import models

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    email = models.EmailField()

class Post(models.Model):
    name = models.CharField(max_length=15)
