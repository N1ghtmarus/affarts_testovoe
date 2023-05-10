from django.contrib import admin

from .models import Flower, Lot


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    list_filter = ('color',)
    search_fields = ('name', 'color')


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = (
        'seller',
        'name',
        'item',
        'quantity',
        'price_per_unit',
        'hide_from_customers'
        )
    list_filter = ('seller', 'hide_from_customers')
    search_fields = ('seller__username', 'item__name')
