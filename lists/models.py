from django.db import models
from django.urls import reverse
from django.conf import settings


class List(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("view_list", args=[self.id])


class Item(models.Model):
    
    text = models.TextField(default="")
    list = models.ForeignKey(List, models.CASCADE, default=None)

    class Meta:
        unique_together = ('list', 'text')
