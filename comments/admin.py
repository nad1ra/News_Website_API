from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'news', 'author_name', 'author_email', 'content', 'is_approved', 'created_at')
    search_fields = ('news', 'author_name', 'content')
