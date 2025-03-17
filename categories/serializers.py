from rest_framework import serializers
from .models import Category


class Meta:
    model = Category
    fields = ['id', 'name', 'desc']