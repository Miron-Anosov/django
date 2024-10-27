from django.core.management.base import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    """Create product."""
    help = 'Creates products information.'

    def handle(self, *args, **options):
        self.stdout.write("Product is creating.")
        data_prod = {
            "prod_1": {
                "name": "Phones",
                "discount": 15,
                "reviews": 3,
                "price": 100
            },
            "product_2": {
                "name": "Laptops",
                "description": "Product is well.",
                "discount": 5,
                "reviews": 45,
                "price": 150
            },

        }

        for user in data_prod.values():
            prod, if_exist = Product.objects.get_or_create(
                name=user.get("name"),
                description=user.get("description"),
                discount=user.get("discount"),
                reviews=user.get("reviews"),
                price=user.get("price")
            )

            if not if_exist:
                self.stdout.write(self.style.ERROR(f"{prod} created!"))
            else:
                self.stdout.write(self.style.SUCCESS(prod))
                self.stdout.write(self.style.SUCCESS('Successfully created a new user!'))
