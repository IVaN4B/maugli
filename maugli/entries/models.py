from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Entry(models.Model):
	class Meta:
		verbose_name_plural = "entries"
	ARTICLE = 'article'
	PAGE = 'page'
	TYPE_CHOICES = (
		(ARTICLE, 'Article'),
		(PAGE, 'Page'),
	)
	title 	= models.CharField(max_length=255)
	text	= models.TextField()
	type	= models.CharField(max_length=255, choices=TYPE_CHOICES,
								default=ARTICLE)
	alias	= models.CharField(max_length=255, blank=True)
	date	= models.DateField()
	def __str__(self):
		return "%s" % (self.title)
