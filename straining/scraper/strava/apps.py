from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class StravaConfig(AppConfig):
    name = 'strava'

    def ready(self):
        if not hasattr(settings, 'STRAVA_CLIENT_ID'):
            raise ImproperlyConfigured(
                "STRAVA_CLIENT_ID Django setting must be set."
            )
        if not hasattr(settings, 'STRAVA_CLIENT_SECRET'):
            raise ImproperlyConfigured(
                "STRAVA_CLIENT_SECRET Django setting must be set."
            )
