from distutils.command.upload import upload
from re import S
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.s
def user_directory_path(instance, filename):
    return f'food/{instance.name}/{filename}'


class Category(models.Model):
    name= models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Food(models.Model):
    state=models.BooleanField(default=False)
    name= models.CharField(max_length=80)
    img= models.ImageField(upload_to=user_directory_path, null=False)
    detail_food= models.TextField(max_length=150)
    slug= models.SlugField(max_length=150, unique_for_date='published', null=False, unique=True)
    published= models.DateField(auto_now_add=True)
    price = models.FloatField(null=False, blank=False) 
    category= models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-name',)
    
    def __str__(self):
        return self.name
    
    