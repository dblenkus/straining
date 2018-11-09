import logging

from asgiref.sync import async_to_sync

from django.shortcuts import get_object_or_404, render

from channels.layers import get_channel_layer
from rest_framework import permissions, serializers, views
from rest_framework.response import Response

from .models import StravaUser
from . import constants, protocol

logger = logging.getLogger(__name__)


class AuthLinkSerializer(serializers.Serializer):
    url = serializers.CharField()


class StartAuthView(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user, _ = StravaUser.objects.get_or_create(user=request.user)
        url = user.get_authorization_url(
            request.build_absolute_uri('/').rstrip('/')
        )
        serializer = AuthLinkSerializer({'url': url})

        return Response(serializer.data)


class CompleteAuthView(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, token_id):
        if 'error' in request.query_params:
            logger.info("")

        user = get_object_or_404(StravaUser, uuid=token_id)
        user.exchange_token(request.query_params['code'])

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.send)(
            protocol.STRAVA_FETCH_CHANNEL,
            {
                'type': protocol.FETCH_ALL_ACTIVITIES_TYPE,
                'stravauser_id': user.id,
            }
        )

        return Response({'status': 'ok'})


class WebhookView(views.APIView):

    permission_classes = ()

    def get(self, request):
        hub_challenge = request.query_params["hub.challenge"]
        return Response({"hub.challenge": hub_challenge})

    def post(self, request):
        if request.data['object_type'] == 'activity':
            channel_layer = get_channel_layer()

            aspect_type = request.data['aspect_type']
            if aspect_type == constants.ASPECT_TYPE_CREATE:
                async_to_sync(channel_layer.send)(
                    protocol.STRAVA_FETCH_CHANNEL,
                    {
                        'type': protocol.FETCH_SINGLE_ACTIVITY_TYPE,
                        'stravauser_id': request.data['owner_id'],
                        'activity_id': request.data['object_id'],
                    }
                )

            if aspect_type == constants.ASPECT_TYPE_UPDATE:
                pass
            if aspect_type == constants.ASPECT_TYPE_DELETE:
                pass

        return Response()
