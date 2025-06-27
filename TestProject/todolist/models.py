from django.db import models
class Todo(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    complete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
# Create your models here.
