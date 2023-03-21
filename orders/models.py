from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=50)
    time_to_cook = models.IntegerField()


class Order(models.Model):

    person_name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, through='OrderProduct')
    is_ready = models.BooleanField(default=False)


class OrderProduct(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
