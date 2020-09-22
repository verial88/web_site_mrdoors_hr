from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Описание новости')
    pub_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-pub_date', )


