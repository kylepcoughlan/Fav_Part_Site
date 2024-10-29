# Messages/management/commands/create_random_notes.py

from django.core.management.base import BaseCommand
from Messages.models import Post  # Adjust import according to your app structure
from faker import Faker

class Command(BaseCommand):
    help = 'Create a specified number of random notes'

    def add_arguments(self, parser):
        parser.add_argument('num_notes', type=int, help='Number of random notes to create')

    def handle(self, *args, **kwargs):
        num_notes = kwargs['num_notes']
        fake = Faker()
        
        for _ in range(num_notes):
            post = Post(
                title=f"Note {Post.objects.count() + 1}",  # Title based on count
                content=fake.text(max_nb_chars=200),
                signed=fake.first_name()
            )
            post.save()
        
        self.stdout.write(self.style.SUCCESS(f'{num_notes} random notes created.'))
