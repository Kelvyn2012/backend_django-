from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")  # Show these columns
    search_fields = ("name", "category")  # Search bar
    list_filter = ("category",)  # Sidebar filter
    ordering = ("-price",)  # Order by price descending


# Register your models here.
admin.site.register(Product, ProductAdmin)
