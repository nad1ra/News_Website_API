from rest_framework import serializers
from .models import Comment
from news.serializers import NewsShortSerializer


class CommentSerializer(serializers.ModelSerializer):
    news = NewsShortSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id', 'news', 'author_name', 'author_email',
            'content', 'is_approved', 'created_at'
        ]
