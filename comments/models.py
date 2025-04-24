from django.db import models
from news.models import News


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, related_name='comments')
    author_name = models.CharField(max_length=50)
    author_email = models.EmailField(unique=True)
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.news}"