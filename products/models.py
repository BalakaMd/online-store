from django.db import models

from users.models import User


class ProductsCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} | id={self.id}'

    class Meta:
        verbose_name_plural = 'Products Categories'


class Products(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ManyToManyField(ProductsCategory)
    image = models.ImageField(upload_to='products_images')

    def __str__(self):
        return f'Product: {self.name} | Description: {self.category.name}'

    def get_categories(self):
        categories = self.category.all()
        return ', '.join([category.name for category in categories])

    class Meta:
        verbose_name_plural = 'Products'


class BaskerQuerySet(models.QuerySet):
    def total_price(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)

    objects = BaskerQuerySet.as_manager()

    def sum(self):
        return self.quantity * self.products.price
