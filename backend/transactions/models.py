from django.db import models
from django.core.exceptions import ValidationError

from users.models import User
from listings.models import Lot


class Transaction(models.Model):
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='buyer_transactions'
        )
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Кол-во товара')
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
        )
    timestamp = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.quantity > self.lot.quantity:
            raise ValidationError("У продавца нет такого кол-ва товара")

    def save(self, *args, **kwargs):
        self.full_clean()
        self.total_price = self.lot.price_per_unit * self.quantity
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ['total_price']
