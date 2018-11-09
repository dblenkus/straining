from django.core.management import BaseCommand

from .utils import delete_subscription


class Command(BaseCommand):
    help = 'Deletes a specific Strava webhook subscription.'

    def add_arguments(self, parser):
        parser.add_argument('id', type=str)

    def handle(self, *args, **options):
        """Deletes a specific Strava webhook subscription."""
        self.stdout.write(
            "Deleting subscription with ID {}".format(options['id'])
        )

        resp = delete_subscription(options['id'])

        if resp.status_code == 204:
            self.stdout.write("Subscription deleted.")
        else:
            self.stderr.write("Failed to delete the subscription.")
