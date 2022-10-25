from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# THIS MODELS file is used create classes which ultimately creates DB and DB Queries
# Create your models here.

class Book(models.Model):   #by taking these below mentioned fields django creates a DB with name BOOK and also has id col by default
    title = models.CharField(max_length = 30)
    rating = models.IntegerField(
        validators = [MinValueValidator(1),MaxValueValidator(5)] ,default = 1
    )
    author = models.CharField(max_length = 35, null=True) #null=True will get executed when there is not value provided 
    is_bestselling = models.BooleanField(default = False) #default = False will get executed when there is not value provided 
    slug = models.SlugField(default = "",blank = True, null= False, db_index= True) # this will provide a slug value
    
    
    #]way to create model specific url's
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    #function below to save the slug inside the db itself
    # def save (self , *args , **kwargs):
    #     self.slug = slugify(self.title) # this function coverts title to the slug (this work is done pre-populate field from admin)
    #     super().save(*args , **kwargs)

    #to get all entries from DB
    def __str__(self):
        return f"{self.title} ({self.rating})"