from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'image', 'views_count', 'is_published', 'created_at', 'updated_at')
    search_fields = ('title', 'slug', 'content')