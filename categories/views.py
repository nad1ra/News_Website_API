from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from .paginations import CategoryPagination

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
