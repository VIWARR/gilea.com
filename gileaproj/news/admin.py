from django.contrib import admin

from news.models import Post
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = (('title', 'author'), 'content')
    list_display = ('title', 'content', 'date_created', 'author')
    list_filter = ('author', )
    form = PostAdminForm
