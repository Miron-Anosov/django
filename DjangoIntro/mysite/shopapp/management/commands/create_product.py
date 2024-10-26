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
        },
           "product_2": {
                "name": "Laptops",
                "description": "Product is well."
            },

        }

        for user in data_prod.values():
            prod, error = Product.objects.get_or_create(
                name=user.get("name"),
                description=user.get("description"),
            )

            if error:
                self.stdout.write(self.style.ERROR("Could not create!"))
            else:
                self.stdout.write(self.style.SUCCESS(prod))
                self.stdout.write(self.style.SUCCESS('Successfully created a new user!'))
