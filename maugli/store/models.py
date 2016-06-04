from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    code         = models.IntegerField()
    name         = models.CharField(max_length=255, blank=True)

class Column(models.Model):
    name        = models.CharField(max_length=255)
    type        = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    value        = GenericForeignKey('type', 'id')

class Product(models.Model):
    code        = models.IntegerField()
    categories  = models.ManyToManyField(Category)
    columns        = models.ManyToManyField(Column)
