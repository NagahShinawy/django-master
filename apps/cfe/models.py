from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.pk}, title={self.title[:20]}, price={self.price})"

    @property
    def sale_price(self):
        return float("%.2f" % (float(self.price) * 0.08))

    @property
    def calc_discount(self):
        return float(self.price) - float(self.sale_price)

    class Meta:
        ordering = ["id"]


class Color(models.Model):
    rgb = models.CharField(max_length=11)
    _hexa = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.rgb} - {self._hexa}"


class Bike(models.Model):
    brand = models.CharField(max_length=100)