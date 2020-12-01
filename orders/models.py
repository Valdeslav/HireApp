from django.db import models
from application.models import Product


class Hire(models.Model):
    hirer = models.PositiveIntegerField()
    slug = models.SlugField(max_length=200, db_index=True)
    taking_date = models.DateField()
    return_date = models.DateField()
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    paid = models.BooleanField(default=False)
    number = models.PositiveIntegerField()

    class Meta:
        ordering = ('return_date',)


class HireElement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, db_index=True)
    number = models.IntegerField()
    hire = models.ForeignKey(Hire, on_delete=models.CASCADE, related_name="elems")

    def get_cost(self):
        return self.product.cost * self.number
