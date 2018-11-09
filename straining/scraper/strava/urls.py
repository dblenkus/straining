from django.urls import include, path

from . import views


app_name = 'strava'
urlpatterns = [
    path(
        'authorize/',
        views.StartAuthView.as_view(),
        name='start-authorization'
    ),
    path(
        'exchangetoken/<uuid:token_id>/',
        views.CompleteAuthView.as_view(),
        name='exchange-token'
    ),
    path(
        'webhook/',
        views.WebhookView.as_view(),
        name='webhook'
    ),
 ]
