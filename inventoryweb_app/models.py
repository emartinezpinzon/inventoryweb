from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(blank=True)
    inventary_min = models.IntegerField()
    price_in = models.IntegerField()
    price_out = models.IntegerField()
    unit = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name