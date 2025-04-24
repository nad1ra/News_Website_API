from rest_framework import serializers
from .models import News
'''from categories.serializers import CategorySerializer
from tags.serializers import TagSerializer'''


class NewsShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'slug']
