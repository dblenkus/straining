import json
import logging
from datetime import datetime, timedelta

import requests

from django.core.files.uploadedfile import SimpleUploadedFile

from channels.consumer import SyncConsumer

from straining.core.models import Activity, ActivityStream

from . import constants
from .models import StravaUser

logger = logging.getLogger(__name__)


class StravaConsumer(SyncConsumer):

    @staticmethod
    def _save_activity(activity, user):
        return Activity.objects.create(
            activity_id=activity['id'],
            user=user,
            name=activity['name'],
            type=activity['type'],
            ride_date=activity['start_date_local'],
            distance=activity.get('distance'),
            average_speed=activity.get('average_speed'),
            average_watts=activity.get('average_watts'),
            average_heartrate=activity.get('average_heartrate'),
            max_heartrate=activity.get('max_heartrate'),
        )

    @staticmethod
    def _get_headers(user):
        return {
            'Authorization': constants.AUTHORIZATION_HEADER.format(
                token=user.get_access_token()
            ),
        }

    def straining_fetch_all(self, event):
        user = StravaUser.objects.get(pk=event['stravauser_id'])

        previous_year = datetime.now() - timedelta(days=365)
        previous_year = previous_year.timestamp()

        headers = self._get_headers(user)
        params = {
            'page': 1,
            'per_page': constants.PER_PAGE_LIMIT,
        }

        logger.info(
            "Fetching all Strava activities for {}.".format(repr(user))
        )

        activities = []
        added_activities = constants.PER_PAGE_LIMIT
        while added_activities == constants.PER_PAGE_LIMIT:
            logger.debug("Fetching Strava activities page {} for {}".format(
                    params['page'], repr(user)
            ))
            response = requests.get(
                constants.ACTIVITIES_URL.format(after=previous_year),
                params=params,
                headers=headers,
            )
            activities_json = response.json()
            activities.extend(activities_json)
            added_activities = len(activities_json)
            params['page'] += 1

        logger.info("Fetched {} Strava activities for {}".format(
            len(activities), repr(user)
        ))

        existing_ids = Activity.objects.filter(
            user=user.user
        ).values_list(
            'activity_id', flat=True
        )

        activities = list(filter(
            lambda activity: activity['id'] not in existing_ids, activities
        ))

        logger.info("Found {} new Strava activities for {}".format(
            len(activities), repr(user)
        ))

        for act in activities:
            self._save_activity(act, user.user)

        user.fetched = True
        user.save()

        logger.info(
            "Done fetching Strava activities for {}.".format(repr(user))
        )

    def straining_fetch_single(self, event):
        user = StravaUser.objects.get(athlete_id=event['stravauser_id'])
        activity_id = event['activity_id']

        headers = self._get_headers(user)

        existing_activity = Activity.objects.filter(activity_id=activity_id)
        if not existing_activity.exists():
            logger.info("Fetching Strava activity %d.", activity_id)

            url = constants.STRAVA_ACTIVITY_URL.format(
                activity_id=activity_id
            )
            activity = requests.get(url, headers=headers).json()
            activity = self._save_activity(activity, user.user)

            logger.info("Done fetching Strava activity %d.", activity_id)

        else:
            logger.info("Strava activity %d already exists.", activity_id)
            activity = existing_activity.first()

        if not hasattr(activity, 'activitystream'):
            logger.info(
                "Fetching streams for Strava activity %d.", activity_id
            )

            stream_url = constants.STRAVA_ACTIVITY_STREAM_URL.format(
                activity_id=activity_id,
                types=constants.STRAVA_STREAM_TYPES,
            )
            response = requests.get(stream_url, headers=headers)
            json_response = response.json()

            activity_stream = ActivityStream()
            activity_stream.activity = activity
            for stream in json_response:
                stream_type = stream['type']
                setattr(
                    activity_stream,
                    stream_type,
                    SimpleUploadedFile(
                        '{}-{}.json'.format(activity.id, stream_type),
                        json.dumps(stream).encode('utf-8'),
                        'application/json',
                    )
                )
            activity_stream.save()

            logger.info(
                "Fetched %d streams for Strava activity %d",
                len(json_response), activity_id
            )
        else:
            logger.info(
                "Streams for Strava activity %d already exists.", activity_id
            )
