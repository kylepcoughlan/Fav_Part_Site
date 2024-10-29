# Messages/management/commands/clear_all_notes.py

from django.core.management.base import BaseCommand
from Messages.models import Post  # Adjust import according to your app structure

class Command(BaseCommand):
    help = 'Delete all notes'

    def handle(self, *args, **kwargs):
        count, _ = Post.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} notes.'))
