from django.contrib import admin

from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'lot', 'quantity', 'total_price', 'timestamp')
    list_filter = ('buyer', 'lot', 'timestamp')
    search_fields = ('buyer__username', 'lot__id')
    readonly_fields = ('total_price',)
