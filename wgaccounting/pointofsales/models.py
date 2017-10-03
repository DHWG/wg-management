from django.db import models
from persons.models import Inhabitant

class Product(models.Model):

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='product_images', null=True, blank=True)

    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'Product: {self.name}'

class Purchase(models.Model):

    date = models.DateTimeField(auto_now_add=True)

    buyer = models.ForeignKey(Inhabitant, on_delete=models.CASCADE, related_name='buyer')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return f'[ {self.buyer.username} bought a {self.product.name} for {self.product.unit_price}€ @ {self.date} ]'