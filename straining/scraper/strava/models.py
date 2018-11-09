import json
import time
import uuid

import requests

from django.conf import settings
from django.db import models
from django.urls import reverse

from fernet_fields import EncryptedTextField

from straining.core.models import Activity
from straining.scraper.exceptions import AuthFailedException

from .constants import STRAVA_AUTHORIZATION_URL, STRAVA_GET_TOKEN_URL


class StravaUser(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4, db_index=True, editable=False,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    access_token = EncryptedTextField()

    expires_at = models.IntegerField(null=True)

    refresh_token = EncryptedTextField()

    athlete_id = models.IntegerField(null=True)

    fetched = models.BooleanField(default=False)

    class Meta:
        db_table = 'scraper_strava_token'

    def __str__(self):
        return "id: {}, athlete_id: {}".format(self.id, self.athlete_id)

    def get_authorization_url(self, redirect_prefix=None):
        redirect_uri = reverse(
            'straining:strava:exchange-token',
            kwargs={'token_id': self.uuid}
        )
        if redirect_prefix:
            redirect_uri = redirect_prefix + redirect_uri

        context = {
            'client_id': settings.STRAVA_CLIENT_ID,
            'redirect_uri': redirect_uri,
        }
        return STRAVA_AUTHORIZATION_URL.format(**context)

    def exchange_token(self, code):
        response = requests.post(
            STRAVA_GET_TOKEN_URL,
            data={
                'client_id': settings.STRAVA_CLIENT_ID,
                'client_secret': settings.STRAVA_CLIENT_SECRET,
                'code': code,
                'grant_type': 'authorization_code',
            },
        )
        response = json.loads(response.text)

        self.access_token = response['access_token']
        self.expires_at = response['expires_at']
        self.refresh_token = response['refresh_token']
        self.athlete_id = response['athlete']['id']

        self.save()

    def get_access_token(self):
        if self.expires_at < time.time() + 600:
            response = requests.post(
                STRAVA_GET_TOKEN_URL,
                data={
                    'client_id': settings.STRAVA_CLIENT_ID,
                    'client_secret': settings.STRAVA_CLIENT_SECRET,
                    'refresh_token': self.refresh_token,
                    'grant_type': 'refresh_token',
                },
            )
            response = json.loads(response.text)

            self.access_token = response['access_token']
            self.expires_at = response['expires_at']
            self.refresh_token = response['refresh_token']

            self.save()

        return self.access_token
