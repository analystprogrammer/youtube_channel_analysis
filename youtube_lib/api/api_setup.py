from decouple import config
import googleapiclient.discovery

channel_id = 'UCD2Xhzch7uhW4sWlLyX4XXw'
YOUTUBE_API_KEY = config('youtube_api_key')

class YoutubeAPI:

    def __init__(self):
        self._id = channel_id
        self.api_version = "v3"
        self._api_key = YOUTUBE_API_KEY
        self.api_service_name = "youtube"
        self.youtube_services = self.setup()

    def setup(self):
        return googleapiclient.discovery.build(self.api_service_name, self.api_version, developerKey= self._api_key)
