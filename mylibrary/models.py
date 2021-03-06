from django.db import models
from django.contrib import admin
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

from django.urls import reverse
from django.db.models.signals import post_save

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length =30)
    author = models.CharField(max_length =50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books", blank=True,null=True)
    description = models.TextField(max_length =200, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    images = CloudinaryField('images')
    def __str__(self):
        return str(self.name)


    def save_library_book(self):
        self.save()

    def delete_library_book(self):
        self.delete()


    @classmethod
    def update_library_book(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
        
    def get_absolute_url(self):
        return reverse('index')

    @classmethod
    def search_category(cls,search_term):
        searched_category = Books.objects.filter(name =search_term)
        return searched_category


class BooksPostAdmin(admin.ModelAdmin):
    readonly_fields = ('status',)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.png')    
    bio = models.TextField(max_length=500, default="My Bio", blank=True)   
    name = models.CharField(blank=True, max_length=120)    
    location = models.CharField(max_length=60, blank=True)    
    email = models.EmailField(max_length=100, blank=True)


    def __str__(self):        
        return f'{self.user.username} Profile'