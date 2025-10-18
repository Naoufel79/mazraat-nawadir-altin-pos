from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Reset admin password'

    def handle(self, *args, **kwargs):
        try:
            user = User.objects.get(username='admin')
            user.set_password('admin123')
            user.save()
            self.stdout.write(self.style.SUCCESS('✓ Admin password reset successfully!'))
            self.stdout.write(self.style.SUCCESS('Username: admin'))
            self.stdout.write(self.style.SUCCESS('Password: admin123'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('Admin user does not exist'))
