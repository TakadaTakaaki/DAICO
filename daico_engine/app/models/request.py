from django.db import models
from django.utils import timezone

class Request(models.Model):
    class Meta:
        db_table = 'request'

    kind = models.CharField(
        max_length=30,
    )
    name = models.CharField(
        max_length=30,
    )
    address = models.CharField(
        max_length=100,
    )
    email = models.EmailField(
        max_length=128,
    )
    message = models.CharField(
        max_length=300,
        null=False
    )
    phone = models.TextField(
        max_length=12,
        null=False
    )


    def __str__(self):
        return self.name