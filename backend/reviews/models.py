from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import User
from listings.models import Lot


class Review(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='seller_reviews'
        )
    lot = models.ForeignKey(
        Lot,
        on_delete=models.CASCADE,
        related_name='lot_reviews',
        null=True,
        blank=True
        )
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='customer_reviews'
        )
    rating = models.PositiveIntegerField(
        'Оценка по пятибальной шкале',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField('Текст отзыва')

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'
        ordering = ['rating']
