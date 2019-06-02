from django.db import models
from django.utils import timezone


class Company_data(models.Model):
    class Meta:
        db_table = 'company_data'

    name = models.CharField(max_length=30)
    pr = models.CharField(max_length=70)
    tell = models.CharField(max_length=12)
    price = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    credit = models.CharField(max_length=50)
    homepage = models.URLField(max_length=100)
    staff = models.CharField(max_length=10)
    time = models.CharField(max_length=20)
    service = models.TextField()
    pay = models.TextField()
    cancel = models.TextField() 
    security = models.TextField()
    place1 = models.CharField(max_length=10)
    place2 = models.CharField(max_length=10)
    
    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.name + ',' + self.staff + '>'

class Staff(models.Model):
    class Meta:
        db_table = 'staff'

    company_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=10)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.company_name

class Plan(models.Model):
    class Meta:
        db_table = 'plan'

    company_plan = models.CharField(max_length=30)
    genre = models.CharField(max_length=8)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=75)
    price = models.CharField(max_length=30)
    terms = models.CharField(max_length=20)
    effect = models.CharField(max_length=15)

    def __str__(self):
        return self.company_plan
