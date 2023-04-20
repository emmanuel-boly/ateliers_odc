from django.contrib import admin
from .models import Post, Comment

"""
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('author', 'date_posted')
    search_fields = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'date_commented')
    list_filter = ('post', 'author', 'date_commented')
    search_fields = ('content',)

"""
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
