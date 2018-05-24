from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, null = True, blank = True)
    Title = models.CharField(max_length=200)
    Description = models.TextField(max_length=200)

    def __str__(self):
        return self.Title

