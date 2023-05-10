from django.db import models

from users.models import User


class Flower(models.Model):
    name = models.CharField(max_length=100)
    COLOR_CHOICES = (
        ('красный', 'Красный'),
        ('синий', 'Синий'),
        ('желтый', 'Желтый'),
    )
    color = models.CharField(
        'Оттенок цветка',
        max_length=10,
        choices=COLOR_CHOICES
        )

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Lot(models.Model):
    name = models.CharField('Название лота', max_length=100)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Кол-во товара')
    price_per_unit = models.DecimalField(
        'Цена за шт.',
        max_digits=10,
        decimal_places=2
        )
    hide_from_customers = models.BooleanField(
        'Не показывать товар покупателям',
        default=False
        )

    class Meta:
        verbose_name = 'Лот'
        verbose_name_plural = 'Лоты'

    def __str__(self):
        return self.name
