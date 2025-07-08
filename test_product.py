import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_django.settings")
django.setup()


from book_store.models import Product

# Create a product
Product.objects.get_or_create(
    name="AirPods",
    defaults={
        "description": "Wireless earbuds by Apple",
        "price": 199.99,
        "category": "Electronics",
    },
)

for product in Product.objects.all():
    print(product.name, "-", product.price)
