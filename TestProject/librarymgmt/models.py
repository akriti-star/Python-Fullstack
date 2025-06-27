from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=11, primary_key=True)
    title = models.CharField(max_length=100,null = False)
    author = models.CharField(max_length=100,null = False)
    publisher = models.CharField(max_length=100,null= False)

