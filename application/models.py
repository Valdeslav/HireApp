from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.FloatField()


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
