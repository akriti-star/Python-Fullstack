from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll_number = models.PositiveSmallIntegerField(primary_key=True)
    address = models.TextField(max_length=100)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.name