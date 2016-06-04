from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

from menu.models import MenuLink
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
	links 	= models.ManyToManyField(MenuLink, blank=True,
									related_name="entry")
	date	= models.DateField()
	def __str__(self):
		return "%s" % (self.title)

	def get_link_list(self):
		return ", ".join([p.title for p in self.links.all()])
	get_link_list.short_description = 'links'
