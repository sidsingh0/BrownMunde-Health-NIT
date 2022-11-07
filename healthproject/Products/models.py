from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150, null=False)
    price = models.FloatField(null=False, default=0.0)
    quantity = models.IntegerField(null=False, default=0)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
