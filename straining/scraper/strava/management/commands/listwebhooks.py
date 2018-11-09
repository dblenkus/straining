import json

from django.core.management import BaseCommand

from .utils import get_subscriptions


class Command(BaseCommand):
    help = 'Lists all Strava webhook subscriptions.'

    def handle(self, *args, **options):
        """List all Strava webhook subscriptions."""
        for subscription in get_subscriptions().json():
            self.stdout.write(json.dumps(subscription))
