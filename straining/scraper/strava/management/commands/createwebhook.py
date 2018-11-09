import json

from django.core.management import BaseCommand

from .utils import create_subscription

def get_callback_url():
    return


class Command(BaseCommand):
    help = 'Creates a new Strava webhook subscription.'

    def handle(self, *args, **options):
        """Create a new Strava webhook subscription."""

        resp = create_subscription()

        # Load and dump content to get nicer formatting.
        content = json.loads(resp.content.decode('utf-8'))
        self.stdout.write(json.dumps(content))

        self.stdout.write(
            "Creating the webhook subscription ended with "
            "status code {}".format(resp.status_code)
        )
