from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.CharField(max_length=300)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])


class Hirer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)


class Hire(models.Model):
    hirer = models.ForeignKey(Hirer, on_delete=models.PROTECT)
    taking_date = models.DateField()
    return_date = models.DateField()
    cost = models.FloatField()


class HireElement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    number = models.IntegerField()
    hire = models.ForeignKey(Hire, on_delete=models.PROTECT)
