from channels.routing import ChannelNameRouter, ProtocolTypeRouter

from straining.scraper.strava.consumers import StravaConsumer
from straining.scraper.strava.protocol import STRAVA_FETCH_CHANNEL


application = ProtocolTypeRouter({

    # Background worker consumers.
    'channel': ChannelNameRouter({
        STRAVA_FETCH_CHANNEL: StravaConsumer,
    })
})
