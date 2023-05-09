from django.db import models

from django.contrib.auth.models import User


class GilDev(models.Model):
    """"CREATE MODEL GILEA DEVELOPMENT"""
    title = models.CharField(verbose_name='Заголовок', max_length=300)
    content = models.TextField(verbose_name='Контент', max_length=10000)
    completion_date = models.DateField(verbose_name='Дата окончания')
    draft = models.BooleanField(verbose_name='Публикация', default=False)

    class Meta:
        verbose_name = 'Планы развития GILEA'
        verbose_name_plural = 'Планы развития GILEA'

    def __str__(self):
        return self.title

class ComStories(models.Model):
    """"CREATE MODEL COMPANY STORIES"""
    title = models.CharField(verbose_name='Заголовок', max_length=300)
    stories = models.TextField(verbose_name='История', max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    draft = models.BooleanField(verbose_name='Публикация', default=False)

    class Meta:
        verbose_name = 'Истории компаний'
        verbose_name_plural = 'Истории компаний'

    def __str__(self):
        return self.title

class Newsroom(models.Model):
    """"CREATE MODEL NEWSROOM"""
    CAT_CHOICES = [
        ('price', 'Новости по ценам'),
        ('market', 'Новости по рынку'),
        ('production', 'Новости по производству'),
        ('trade', 'Новости по торговле'),
        ('without', 'Без категории'),
    ]

    title = models.CharField(verbose_name='Заголовок', max_length=300)
    content = models.TextField(verbose_name='Контент', max_length=10000)
    category = models.CharField(verbose_name='Категория', max_length=25, choices=CAT_CHOICES, default='without')
    data_created = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    draft = models.BooleanField(verbose_name='Публикация', default=False)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title