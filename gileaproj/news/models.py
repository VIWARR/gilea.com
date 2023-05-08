from django.db import models

from django.contrib.auth.models import User
from gileaproj.settings import TIME_ZONE


class Post(models.Model):
    """CREATING A POST MODEL"""
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, default=TIME_ZONE.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'create post'
        verbose_name_plural = 'create posts'

    def __str__(self):
        return self.title