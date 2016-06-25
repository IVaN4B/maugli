from django.db import models

from conf import settings

class Menu(models.Model):
    name   = models.CharField(max_length=255)
    title  = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return "%s" % (self.title)

class MenuLink(models.Model):
    title =    models.CharField(max_length=255)
    url      = models.CharField(max_length=255)
    menu  = models.ManyToManyField(Menu, blank=True, related_name="links")
    weight = models.IntegerField(default=0)
    def __str__(self):
        return "%s" % (self.title)

    def get_absolute_url(self):
        return settings.URL_ROOT+self.url

    def get_menu_list(self):
        return ", ".join([p.title for p in self.menu.all()])

    def get_entry_list(self):
        return ", ".join([p.title for p in self.entry.all()])
