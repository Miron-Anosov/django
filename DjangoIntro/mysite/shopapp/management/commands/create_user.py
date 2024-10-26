from django.core.management.base import BaseCommand
from shopapp.models import User


class Command(BaseCommand):
    """Create a new user."""

    def handle(self, *args, **options):
        self.stdout.write("User is creating.")
        data_user = {
            "user_1": {
            "name": "Ivan",
            "surname": "Ivanov",
            "age": 25
        },
           "user_2": {
                "name": "Petr",
                "surname": "Petrov",
                "age": 35
            },

        }
        for user in data_user.values():
            user_db, error = User.objects.get_or_create(
                name=user.get("name"),
                surname=user.get("surname"),
                age=user.get("age"),
            )

            if error:
                self.stdout.write(self.style.ERROR("Could not create!"))
            else:
                self.stdout.write(self.style.SUCCESS(user_db))
                self.stdout.write(self.style.SUCCESS('Successfully created a new user!'))
