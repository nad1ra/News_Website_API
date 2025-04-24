from rest_framework import viewsets
from .models import News
from .serializers import NewsShortSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .paginations import NewsPagination
from comments.serializers import CommentSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsShortSerializer
    pagination_class = NewsPagination

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        news = self.get_object()
        news.is_published = True
        news.save()
        return Response({'status': 'News published successfully'}, status=200)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        news = self.get_object()
        comments = news.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)