from rest_framework import serializers
from .models import New


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['id', 'title', 'content', 'category', 'tags', 'image', 'is_published']