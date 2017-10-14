from django.core.management.base import BaseCommand, CommandError
from persons.models import Inhabitant

class Command(BaseCommand):
    help = 'Adds a user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, username=None, **options):
        Inhabitant.objects.create(username=username,
                                  password='UNUSED',
                                  is_staff=True)