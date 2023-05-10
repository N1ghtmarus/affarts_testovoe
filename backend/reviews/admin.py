from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'lot', 'customer', 'rating')
    list_filter = ('seller', 'lot', 'customer')
    search_fields = ('seller__username', 'lot__id', 'customer__username')
    readonly_fields = ('id',)
