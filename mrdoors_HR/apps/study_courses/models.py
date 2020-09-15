from django.db import models

# Create your models here.

class Study_course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    create_date = models.DateField(auto_now_add=True)
