from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

class YoutubeAPIClient:

    def __init__(self, api_key):
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_video_data(self, vid):
        ret = None

        response = self.youtube.videos().list(id=vid, part='id,snippet,statistics').execute()
        items = response.get('items')

        if items != None and len(items) >= 1:
            snippet = items[0].get('snippet')
            statistics = items[0].get('statistics')

            if snippet != None and statistics != None:
                print(snippet)
                ret = {
                    'title': snippet.get('title'),
                    'view_count': statistics.get('viewCount'),
                    'like_count': statistics.get('likeCount'),
                    'dislike_count': statistics.get('dislikeCount'),
                    'like_percent': str(int(statistics.get('likeCount')) / (int(statistics.get('likeCount')) + int(statistics.get('dislikeCount'))) * 100) + '%'

                }
                print('動画のタイトル：', snippet.get('title'))
                print('statistics', statistics)
        
        return ret
