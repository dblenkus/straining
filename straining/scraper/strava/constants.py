AUTHORIZATION_HEADER = "Bearer {token}"

STRAVA_AUTHORIZATION_URL = 'https://www.strava.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=activity:read_all'
STRAVA_GET_TOKEN_URL = 'https://www.strava.com/oauth/token'

ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities?after={after}"
STRAVA_ACTIVITY_URL = 'https://www.strava.com/api/v3/activities/{activity_id}'
STRAVA_ACTIVITY_STREAM_URL = 'https://www.strava.com/api/v3/activities/{activity_id}/streams/{types}'
WEBHOOK_API_URL = 'https://api.strava.com/api/v3/push_subscriptions'

PER_PAGE_LIMIT = 50
STRAVA_STREAM_TYPES = ','.join([
    'time', 'latlng', 'distance', 'altitude', 'velocity_smooth', 'heartrate',
    'cadence', 'watts', 'temp', 'moving', 'grade_smooth'
])

ASPECT_TYPE_CREATE = 'create'
ASPECT_TYPE_UPDATE = 'update'
ASPECT_TYPE_DELETE = 'delete'
