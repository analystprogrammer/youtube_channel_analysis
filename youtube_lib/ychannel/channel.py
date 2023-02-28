import json
import pandas as pd
from youtube_lib.api.api_setup import YoutubeAPI
from youtube_lib.yvideos.videos import YVideos


def get_basic_channel_stats(channel_data):
    def get_df_of_channel(self):
        for items in channel_data(self)['items']:
            return pd.DataFrame([{
                'channelName':items['snippet']['title'],
                'subscribers':items['statistics']['subscriberCount'],
                'views': items['statistics']['viewCount'],
                'totalVideos': items['statistics']['videoCount'],
                'playlistId': items['contentDetails']['relatedPlaylists']['uploads']
            }])
    return get_df_of_channel

class YChannel(YoutubeAPI,YVideos):

    def __init__(self):
        YoutubeAPI.__init__(self)
        YVideos.__init__(self,self.youtube_services,self._id)

    @get_basic_channel_stats
    def get_channel_details(self):
        youtube = self.youtube_services
        api_request = youtube.channels().list(
            part="snippet, contentDetails, statistics",
            id = self._id
        )
        # print(json.dumps(api_request.execute(), indent = 4))
        response = api_request.execute()
        return response



if __name__ == "__main__":
    obj = YChannel()
    # print(obj.get_channel_details())
    obj.get_channel_videos_details()
