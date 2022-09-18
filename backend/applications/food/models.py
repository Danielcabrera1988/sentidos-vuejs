from django.db import models
from django.contrib.auth.models import User
# Create your models here

class Food(models.Model):
    state=models.BooleanField(default=False)
    name= models.CharField(max_length=80)
    img= models.ImageField(null=False)
    detail_food= models.TextField(max_length=150)
    slug= models.SlugField(max_length=150, unique_for_date='published', null=False, unique=True)
    published= models.DateField(auto_now_add=True)
    price = models.FloatField(null=False, blank=False) 

    class Meta:
        ordering = ('-name',)
    
    def __str__(self):
        return self.name
    
    