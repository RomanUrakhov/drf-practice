from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Generates five fake users for the application"

    def handle(self, *args, **options):
        result = []
        for i in range(0, 5):
            result.append(User.objects.create(login=f'user{i}', password=123))
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created fake users: {result}')
        )
