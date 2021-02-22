from django.db import models
import datetime as dt
from django.urls import reverse

# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField() 

class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'posts/')
    content = models.TextField(blank=True)
    writer = models.ForeignKey('UserProfile', on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    likes = models.ManyToManyField(UserProfile, related_name='post_writer')
    category = models.CharField(max_length=50, default='coding')
    
    def get_absolute_url(self):
        return reverse('home')

    def total_likes():
        return self.likes.count()
        

    
    
    

