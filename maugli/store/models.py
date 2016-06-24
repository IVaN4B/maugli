from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    code        = models.IntegerField()
    name        = models.CharField(max_length=255, blank=True)

class AbstractColumn(models.Model):
    class Meta:
        abstract = True
    STRING  = "string"
    INT     = "int"
    DECIMAL = "decimal"
    TEXT    = "text"
    TYPE_CHOICES = (
        (STRING,  "String"),
        (INT,     "Integer"),
        (DECIMAL, "Decimal"),
        (TEXT,    "Text"),
    )
    #type        = models.CharField(max_length=255, choices=TYPE_CHOICES,
    #                                               default=STRING)

class TitleColumn(AbstractColumn):
    class Meta:
        verbose_name = 'title'
    value       = models.CharField(max_length=255, blank=True)

class PriceColumn(AbstractColumn):
    class Meta:
        verbose_name = 'price'
    value       = models.DecimalField(max_digits=20, decimal_places=2)

class Product(models.Model):
    code        = models.IntegerField()
    categories  = models.ManyToManyField(Category)
    title       = models.ForeignKey(TitleColumn, on_delete=models.CASCADE)
    price       = models.ForeignKey(PriceColumn, on_delete=models.CASCADE)
    def get_title(self):
        return self.title.value
    def get_price(self):
        return self.price.value
    def get_image_url(self):
        domain = "http://maugli-toys.com"
        return "%s/photos/%s.jpg" % (domain, self.code)
