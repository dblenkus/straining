from django.urls import include, path

urlpatterns = [
    path(
        '',
        include('straining.urls', namespace='straining')
    ),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
 ]
