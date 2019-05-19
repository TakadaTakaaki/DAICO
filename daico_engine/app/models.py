from django.db import models
from django.utils import timezone

class Article(models.Model):
    class Meta:
        db_table = 'article'

    title = models.CharField(max_length=20)
    genre = models.CharField(max_length=4)
    date = models.DateTimeField()
    body = models.TextField()

class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            post_count=models.Count('post')
        ).order_by('-post_count')

class Category(models.Model):
    class Meta:
        db_table = 'category'

    name = models.CharField(max_length=40)
    objects = CategoryManager()

    def __str__(self):
        if hasattr(self, 'post_count'):
            return f'{self.name}({self.post_count})'
        else:
            return self.name

class Post(models.Model):
    class Meta:
        db_table = 'post'

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=4)
    published = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='media/')
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT,)

    def __str__(self):
        return self.title
