from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

class YoutubeAPIClient:

    def __init__(self, api_key):
        self.youtube = build('youtube', 'v3', developerKey=api_key)
    
    def get_video_datas_from_channel(self, cid, *, maxResults=10, order='date'):
        ret = []

        response = self.youtube.search().list(channelId=cid, part='id', maxResults=maxResults, order=order).execute()
        
        items = response.get('items')
        if items is not None and len(items) >= 1:
            for item in items:
                id = item.get('id')
                if id is not None:
                    target_video_id = id.get('videoId')
                    if target_video_id is not None:
                        ret.append(self.get_video_data(target_video_id))
        return ret

    def get_video_data(self, vid):
        ret = None

        response = self.youtube.videos().list(id=vid, part='snippet,statistics').execute()
        items = response.get('items')

        if items is not None and len(items) >= 1:
            snippet = items[0].get('snippet')
            statistics = items[0].get('statistics')

            if snippet is not None and statistics != None:
                print(snippet)
                ret = {
                    'published': snippet.get('publishedAt'),
                    'title': snippet.get('title'),
                    'view_count': statistics.get('viewCount'),
                    'like_count': statistics.get('likeCount'),
                    'dislike_count': statistics.get('dislikeCount'),
                    'like_percent': self.culc_like_percent(statistics.get('likeCount'), statistics.get('dislikeCount'))

                }
        return ret

    def culc_like_percent(self, like, dislike):
        l = float(like)
        dl = float(dislike)

        ratio = l / (l + dl)
        percent = round(ratio, 4) * 100
        
        return str(percent) + '%'

