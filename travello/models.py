from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.FloatField(null=False)
    image = models.ImageField(upload_to='pic')
    offer = models.BooleanField(default=False)
