from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=70)
    category = models.ForeignKey(Category, blank=True, null=True)
    description = models.TextField(blank=True)
    inventary_min = models.IntegerField()
    price_in = models.IntegerField()
    price_out = models.IntegerField()
    unit = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name