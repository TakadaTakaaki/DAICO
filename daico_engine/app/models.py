from django.db import models
from django.utils import timezone



# class article(models.Model):
#     class Meta:
#     db_table = 'article'

#     title = models.CharField(max_length=20)
#     genre = models.CharField(max_length=4)
#     date = models.DateTimeField(default=timezone.now)
#     body = models.TextField()

# class post(models.Model):
#     class Meta:
#     db_table = 'post'

#     title = models.CharField(max_length=100)
#     genre = models.CharField(max_length=4)
#     published = models.DateField()
#     body = models.TextField()

#     def __str__(self):
#     return self.title

class Article(models.Model):
    class Meta:
        db_table = 'article'

    title = models.CharField(max_length=20)
    genre = models.CharField(max_length=4)
    date = models.DateTimeField()
    body = models.TextField()

# class post(models.Model):
#     class Meta:
#         db_table = 'post'

#     title = models.CharField(max_length=100)
#     genre = models.CharField(max_length=4)
#     published = models.DateField()
#     body = models.TextField()

#     def __str__(self):
#         return self.title

# class Category(models.Model):
#     class Meta:
#         db_table = 'category'

#     category = models.CharField(max_length=40)

#     def __str__(self):
#         return self.category

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
        if hasattr(self,'post_count'):
            # return f'{self.category}({self.post_count})'
            return f'{self.name}({self.post_count})'
        else:
            return self.name

    # def __str__(self):
    #     return self.category

    # def get_or_create_helper_category():
    #     category, _ = Category.objects.get_or_create(name='家事代行')
    #     return category


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


# class CategorytList(generic.ListView):
#     model = Category

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         # カテゴリを、紐づいた記事数と一緒に取得し、その記事数順に並び替え
#         return queryset.annotate(post_count=Count('post')).order_by('-post_count')

# Create your models here.
