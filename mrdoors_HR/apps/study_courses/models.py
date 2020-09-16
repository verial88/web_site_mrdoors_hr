from django.db import models

# Create your models here.

class Study_course(models.Model):

    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    duration = models.IntegerField('Длительность, мин.', default=0)
    price = models.FloatField('Стоимость, руб.', default=0)
    seats = models.IntegerField('Количество мест', default=0)
    form_event = models.CharField('Форма проведения', max_length=7, default='')
    teacher = models.CharField('Тренер, ФИО', max_length=255, default='')
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Изучаемый курс'
        verbose_name_plural = 'Изучаемые курсы'
