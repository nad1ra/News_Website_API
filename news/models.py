from django.db import models
from categories.models import Category
from tags.models import Tag
from django.utils.text import slugify


class News(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    image = models.ImageField(upload_to='news_image')
    views_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)


    def __str__(self):
        return self.title