from django.contrib.auth import get_user_model, login
from django.core.mail import send_mail
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(email="ilya@gmail.ru", username="2282")
        user.set_password("1234")
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created admin user with email {user.email}"
            )
        )
