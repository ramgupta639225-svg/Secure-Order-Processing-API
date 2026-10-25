from django.db import models
from products.models import Product


class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name="inventory")
    quantity = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(quantity__gte=0), name="inventory_quantity_non_negative"),
        ]

    def __str__(self):
        return f"{self.product.name} - Stock: {self.quantity}"
