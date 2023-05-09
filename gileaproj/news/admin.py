from django.contrib import admin

from news.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = (('title', 'author'), 'content')
    list_display = ('title', 'content', 'date_created', 'author')
    list_filter = ('author', )
