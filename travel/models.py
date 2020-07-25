from django.db import models

# Create your models here.


class Cities(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.CharField(max_length=2048)

    def __str__(self):
        return self.name
