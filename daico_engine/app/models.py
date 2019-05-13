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

class article(models.Model):
    class Meta:
        db_table = 'article'

        title = models.CharField(max_length=20)
        genre = models.CharField(max_length=4)
        date = models.DateTimeField()
        body = models.TextField()

class post(models.Model):
    class Meta:
        db_table = 'post'

        title = models.CharField(max_length=100)
        genre = models.CharField(max_length=4)
        published = models.DateField()
        body = models.TextField()

        def __str__(self):
            return self.title
# Create your models here.
