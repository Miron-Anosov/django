from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Create a new user."""
    def handle(self, *args, **options):
        self.stdout.write("User is creating.")
        self.stdout.write(self.style.SUCCESS('Successfully created a new user!'))
