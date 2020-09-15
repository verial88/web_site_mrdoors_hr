from django.db import models

# Create your models here.

class Student(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    birthday = models.DateField()
    create_date = models.DateField(auto_now_add=True)

