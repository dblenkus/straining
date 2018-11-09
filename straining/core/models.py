from django.conf import settings
from django.db import models

from . import constants

class Activity(models.Model):

    activity_id = models.IntegerField(null=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    name = models.CharField(null=True, max_length=255)

    type = models.CharField(max_length=30)

    ride_date = models.DateTimeField()

    distance = models.FloatField(null=True)

    average_speed = models.FloatField(null=True)

    average_watts = models.FloatField(null=True)

    average_heartrate = models.FloatField(null=True)

    max_heartrate = models.IntegerField(null=True)


class ActivityStream(models.Model):

    activity = models.OneToOneField(
        Activity,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    time = models.FileField(upload_to=constants.ACTIVITIES_MEDIA_PATH)

    latlng = models.FileField(upload_to=constants.ACTIVITIES_MEDIA_PATH)

    distance = models.FileField(upload_to=constants.ACTIVITIES_MEDIA_PATH)

    altitude = models.FileField(upload_to=constants.ACTIVITIES_MEDIA_PATH)

    celocity_smooth = models.FileField(
        upload_to=constants.ACTIVITIES_MEDIA_PATH
    )

    heartrate = models.FileField(upload_to=constants.ACTIVITIES_MEDIA_PATH)

    cadende = models.FileField(upload_to=constants.ACTIVITIES_MEDIA_PATH)

    watts = models.FileField(upload_to=constants.ACTIVITIES_MEDIA_PATH)

    temp = models.FileField(upload_to=constants.ACTIVITIES_MEDIA_PATH)

    moving = models.FileField(upload_to=constants.ACTIVITIES_MEDIA_PATH)

    grade_smooth = models.FileField(upload_to=constants.ACTIVITIES_MEDIA_PATH)
