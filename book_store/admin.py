from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    search_fields = ("name", "category")
    list_filter = ("category",)
    ordering = ("-price",)


# Register your models here.
admin.site.register(Product, ProductAdmin)
