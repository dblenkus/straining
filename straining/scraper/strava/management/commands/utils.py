import requests

from django.conf import settings
from django.urls import reverse

from straining.scraper.strava import constants


def get_subscriptions():
    params = {
        'client_id': settings.STRAVA_CLIENT_ID,
        'client_secret': settings.STRAVA_CLIENT_SECRET,
    }
    resp = requests.get(constants.WEBHOOK_API_URL, params=params)
    return resp


def create_subscription():
    callback_url = 'http://straining.blenkus.com{}'.format(reverse('straining:strava:webhook'))

    data = {
        'client_id': settings.STRAVA_CLIENT_ID,
        'client_secret': settings.STRAVA_CLIENT_SECRET,
        'callback_url': callback_url,
        'verify_token': 'STRAVA'
    }
    resp = requests.post(constants.WEBHOOK_API_URL, data=data)
    return resp


def delete_subscription(subscription_id):
    params = {
        'client_id': settings.STRAVA_CLIENT_ID,
        'client_secret': settings.STRAVA_CLIENT_SECRET,
    }
    resp = requests.delete(
        '{}/{}'.format(constants.WEBHOOK_API_URL, subscription_id),
        params=params
    )
    return resp
