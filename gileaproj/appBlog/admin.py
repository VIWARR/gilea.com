from django.contrib import admin

from appBlog.models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class GilDevAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())
    class Meta:
        model = GilDev
        fields = '__all__'

@admin.register(GilDev)
class GilDevAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'completion_date')

@admin.register(Newsroom)
class NewsroomAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'data_created', 'author')

@admin.register(ComStories)
class ComStoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'stories', 'author')
