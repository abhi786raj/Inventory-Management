from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity', 'price')  # Specify fields to display in the list view
    search_fields = ('name',)  # Enable search by name