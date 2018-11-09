from django.urls import include, path

from rest_framework import routers


api_router = routers.DefaultRouter(trailing_slash=False)

app_name = 'straining'
urlpatterns = [
    path('strava/', include('straining.scraper.strava.urls')),
]
