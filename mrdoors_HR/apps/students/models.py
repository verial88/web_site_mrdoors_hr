from django.db import models


# Create your models here.

class Student(models.Model):
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    begin_work_date = models.DateField('Дата начала работы')
    email_address = models.EmailField('e-mail', null=True, blank=True)
    work_experience = models.FloatField('Стаж работы, мес', default=0)
    phone_number = models.CharField('Телефон', max_length=12, blank=True)
    salone_code = models.IntegerField('Код салона', default=0)
    photo = models.ImageField('Фото', null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
