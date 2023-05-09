from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    """CREATING A POST MODEL"""
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title