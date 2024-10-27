from django.core.management.base import BaseCommand
from shopapp.models import Order
from shopapp.models import Product
from shopapp.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Creating order...")
        user = User.objects.get(id=1)
        product = Product.objects.all()
        order, created = Order.objects.get_or_create(
            name="Bottle of water",
            address="Moscow, Beautiful st 1620",
            user=user,
        )

        if not created:
            self.stdout.write(self.style.ERROR(f"{order} created!"))
        else:
            self.stdout.write(self.style.SUCCESS(order))
            self.stdout.write(self.style.SUCCESS('Successfully created a new user!'))

        self.stdout.write("Creating relationship with products...")
        order = Order.objects.first()

        if order:
            print(product)
            for product in product:
                print(product)
                order.product.add(product)
                order.save()
                self.stdout.write(self.style.SUCCESS(order))
                self.stdout.write(self.style.SUCCESS('Successfully created a new relationship!'))
        else:
            self.stdout.write(self.style.ERROR("Could not create a new relationship!"))