import datetime

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def check_inactive_users():
    today = timezone.now().date()
    inactive_date = today - datetime.timedelta(days=30)
    inactive_users = User.objects.filter(
        is_active=False,
        is_staff=False,
        is_superuser=False,
        last_login__isnull=False,
        last_login__lt=inactive_date,
    ).update(is_active=False)

    for user in inactive_users:
        if user.last_login__lt >= 30:
            user.save()
