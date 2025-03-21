from django.db import models
from django.conf import settings
from accounts.models import User
class Post(models.Model):

    CHOICES = [
        ('landing', 'landing page'),
        ('e-commerce', 'e-commerce'),
        ('mobile', 'mobile app'),
        ('logo design', 'logo design'),
        ('icons', 'icons'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postImage = models.FileField(upload_to='posts/')
    category = models.CharField(max_length=50 ,choices= CHOICES, default='other')

    def __str__(self):
        return f"author : {self.user.username} | category: {self.category}"