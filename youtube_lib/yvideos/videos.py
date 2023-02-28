import os
import json
import pandas as pd
from dotenv import load_dotenv
from youtube_lib.utils.regex import Regex

load_dotenv()

#Get channel videos details csv file path
IMAN_GADZHI_MOMENTS = os.getenv('IMAN_GADZHI_MOMENTS')

class YVideos:

    def __init__(self,youtube_services,id):
        self.youtube_services = youtube_services
        self._id = id
        self.videos_ids = []
        self.all_video_info = []
        self.count = 0

    def get_video_ids(self,details_list_of_videos):
        for videos_details in details_list_of_videos['items']:
            try:
                self.videos_ids.append(videos_details["id"]["videoId"])
            except:
                pass
        return self.videos_ids

    def get_channel_videos_details(self,next_page_token = '',count = 0):
        youtube = self.youtube_services
        api_request = youtube.search().list(
        maxResults=5,
        part="snippet",
        order="viewCount",
        channelId= self._id,
        pageToken = next_page_token
        )
        # print(json.dumps(api_request.execute(), indent=4))
        details_list_of_videos = api_request.execute()

        self.videos_ids = self.get_video_ids(details_list_of_videos)
        next_page_token = details_list_of_videos.get('nextPageToken')
        while next_page_token is not None:
            self.count = count 
            if self.count == 1:
                break
            self.videos_ids = self.get_channel_videos_details(next_page_token,self.count + 1)
            break

        return self.videos_ids


    
    def get_details_of_videos(self):
        self.get_channel_videos_details()
        youtube = self.youtube_services
        api_request = youtube.videos().list(
        part="snippet,contentDetails, statistics",
        id=','.join(self.videos_ids)
        )
        videos_details = api_request.execute()
        # print(json.dumps(videos_details, indent=4))

        for video in videos_details['items']:
            
            stats_to_keep = {'snippet': ['channelTitle', 'title', 'description', 'tags', 'publishedAt'],
                             'statistics': ['viewCount', 'likeCount', 'favouriteCount', 'commentCount'],
                             'contentDetails': ['duration', 'definition', 'caption']
                            }

            video_info = {}
            video_info['video_id'] = video['id']

            for key in stats_to_keep.keys():
                for headers in stats_to_keep[key]:
                    try:
                        if headers == 'duration':
                            print(video[key][headers])
                            video_info[headers] = Regex.convert_to_date(video[key][headers])
                        else:
                            video_info[headers] = video[key][headers]  
                    except:
                        video_info[headers] = None

            self.all_video_info.append(video_info)

        pd.DataFrame(self.all_video_info).to_csv(IMAN_GADZHI_MOMENTS)

