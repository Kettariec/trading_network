from django.core.management import BaseCommand
from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=input('Введите email\n'),
            is_active=True,
        )

        user.set_password(input('Введите пароль\n'))
        user.save()
