from django.db import models
from conf import settings

class Menu(models.Model):
	name   = models.CharField(max_length=255)
	title  = models.CharField(max_length=255, blank=True)
	def __str__(self):
		return "%s" % (self.title)
class MenuLink(models.Model):
	title =	models.CharField(max_length=255)
	url	  = models.CharField(max_length=255)
	menu  = models.ForeignKey(Menu, on_delete=models.CASCADE, default=1,
									related_name="links")
	def __str__(self):
		return "%s" % (self.title)

	def get_url(self):
		return settings.URL_ROOT+self.url
